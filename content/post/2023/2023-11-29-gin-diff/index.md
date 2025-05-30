---
title: gin.vimでgitの差分を快適に閲覧する
author: atusy
date: '2023-11-29'
slug: gin-diff
categories: [Tech]
tags: [Vim, Neovim, Git]
output:
  blogdown::html_page:
    md_extensions: +east_asian_line_breaks+task_lists
highlightjs: [lua]
---

2023/11/29の[Vim駅伝](https://vim-jp.org/ekiden/)記事です。
前回はyasunori0418さんによる「[vimを切っ掛けにエンジニアになった話](https://zenn.dev/vim_jp/articles/0002-engineer_with_vim)」でした。

[gin.vim](https://github.com/lambdalisue/gin.vim)というVim上でGitを便利に扱うプラグインがあります。
水銀などのギンではなく、お酒のジンです。

Exコマンドの`Gin`を通じて、`git`コマンドを実行するのが素朴な使い方です（例：`Gin commit`）。
`Gin`の代わりに`GinBuffer`を使うと、コマンドの実行結果をバッファに出力できます（例：`GinBuffer log -n 1`）。

この2つがあれば、`:!git ...`としていた操作を一通り賄えますが、[gin.vim](https://github.com/lambdalisue/gin.vim)は他にも便利なExコマンドがたくさん用意しています。
以下は一部の例です。

-   `GinDiff`: `git diff`の結果をバッファに出力
-   `GinLog`: `git log`の結果をバッファに出力
-   `GinPatch`: バッファのdiffを対話的にstage/unstageするUIを提供
-   `GinBrowse`: GitHubなどのホスティングサイトで管理されているバッファをブラウザで表示

どれもよく使いますが、イチ推しは`GinDiff`です。

## シンタックスハイライトや単語の差分が見える

カスタマイズすると、以下のようにカラフルな差分を閲覧できます。

![](images/gin-diff-customized.png)

[gin.vim](https://github.com/lambdalisue/gin.vim)の多くのExコマンドは`++processor`引数を通じて実行結果を後処理した結果を取得できます。
そこで、[delta](https://github.com/dandavison/delta)という差分の見た目を調整してくれるプログラムを使うと、シンタックスハイライトや、単語単位の差分を可視化できるというわけです。

おすすめな実行方法は以下。

``` vim
GinDiff ++processor=delta\ --no-gitconfig\ --color-only
```

単に`++processor=delta`としてもカラフルですが、unified diffというパース可能な差分フォーマットではなくなります。
後述の[差分の指定箇所を元ファイルのバッファで開ける](#差分の指定箇所を元ファイルのバッファで開ける)を実現するためには、`--color-only`オプションでunified diffフォーマットを維持するべきです。
また、`delta`コマンドは設定を`gitconfig`ファイルに記載可能ですが、同様の理由で邪魔な設定になりうるので、`--no-gitconfig`オプションでをつけておくといいです。

なお、Neovimユーザーであれば、[tree-sitter-unifieddiff](https://github.com/monaqa/tree-sitter-unifieddiff)も適用すると、もっとカラフルにできます。

先の画像の1行目や2行目がハイライトされたのはまさに`tree-sitter-unifieddiff`の力です。
それから、[gin.vim](https://github.com/lambdalisue/gin.vim)の限界なのかもしれませんが、差分発生箇所の背景色の付き方が不完全なケースがあります。
そこは`tree-sitter-unifieddiff`によるパース結果を[tsnode-marker.nvim](https://github.com/atusy/tsnode-marker.nvim)というプラグインを使って補正しています。

## 差分の指定箇所を元ファイルのバッファで開ける

差分（画像なら背景色が緑や赤になっている場所）で`<CR>`してみましょう。
addedな箇所で`<CR>`すると、差分が発生しているファイルの該当個所に飛びます。
deletedな箇所で`<CR>`すると、差分発生前のファイルの該当箇所に飛びます。

たとえば、以下の画像の`"+  https://github.com/tpope/vim-repeat",`となっている場所で`<CR>`すると、`dot_config/nvim/lua/plugins.lua`の15行目に飛ぶわけですね。

![](images/gin-diff-customized.png)

実体としては`<Plug>(gin-diffjump-smart)`というマッピングを利用しています。
従ってお好みのマッピングへの変更も可能です。

まだ模索中ですが、`<Plug>(gin-diffjump-smart)`をうまく使うと、diff上から定義ジャンプなんてことも可能です。とてもレビューが捗りそうですね。

``` lua
-- Neovimの場合
vim.keymap.set(
  "n",
  "gd",
  "<Plug>(gin-diffjump-smart)<Cmd>lua vim.lsp.buf.definition()<CR>",
  { buffer = true, silent = true }
)
```

## まとめ

[gin.vim](https://github.com/lambdalisue/gin.vim)はいいぞ。
`GinDiff`はカラフルにできるしあちこちジャンプできて体験がいいぞ。
