---
title: gin.vimで捗るgitのログ改竄 (instant fixup)
author: atusy
date: '2024-03-15'
slug: instant-fixup-with-gin-vim
categories: [Vim]
tags: []
output:
  blogdown::html_page:
    md_extensions: +east_asian_line_breaks+task_lists
---

[Vim 駅伝](https://vim-jp.org/ekiden/)の2024/3/15の記事です。

Gitで整然とコミットを詰むのはそうそうたやすいものではありません。
あのコミットでバグを仕込んでしまった、コミットメッセージを間違えていた、そんなミスはよくあることです。
かと言って、整然とコミットするためにコミットを後回しにしては本末転倒です。
うかつな操作で作業内容を失うかもしれませんし、少し前の作業内容に戻りたくなるかもしれません。
また差分が大きくなるほど適切な粒度でのコミットが億劫になります。

そこで、VimでGitを操作するための[gin.vim](https:github.com/lambdalisue/gin.vim)というプラグインを使い、コミットの修正を簡単にする**instant fixup**を実装しました。
magitの[instant fixup](https://magit.vc/manual/magit/Initiating-a-Commit.html)やlazygitの[Amend an old commit](https://github.com/jesseduffield/lazygit?tab=readme-ov-file#amend-an-old-commit)に類する機能です。

# デモ

以下の動画のように、特定のコミットに後から差分を追加したり、メッセージを変更したりできます。
便利なので使ってみてください。

<video autoplay controls>
<source src=./video/demo.mp4>
</video>

**instant fixup**を使えると、とりあえずコミットを積んで後から改竄が容易です。
改竄しやすいコミットの積み方は意識した方がいいかもしれません。
本質的には`git rebase`をしているのですが、大規模なrebaseはコンフリクトの元です。
instantにできることはさっさとやっておくと、コミットの並べ替えや合体といった複雑な操作を後から集注してできるのも魅力ですね。

# 解説

具体的な手順は以下のような感じ

1.  修正したいコミットに混ぜたい変更をステージングしておく

-   ステージング方法は任意。[gin.vim](https:github.com/lambdalisue/gin.vim)を使う場合はファイル単位なら`:GinAdd`や`:GinStatus`、パッチ単位なら`:GinPatch {path}`が便利。
    [gitsigns.nvim](https://github.com/lewis6991/gitsigns.nvim)を使えばバッファ上でカーソル位置のhunkやVisualモードで選択した範囲のステージングもできる。

1.  `:GinLog`を使ってログを表示する

-   `git log`相当。`:GinLog --graph --oneline -n 20`などとオプションの指定も可能

1.  修正したいコミットにカーソルを合わせて`a`（`<Plug>(gin-action-choice)`）を実行する
2.  修正方法に合わせて必要な**instant fixup**を選択

-   `fixup:instant-fixup`: ステージングした差分を選択したコミットに追加
-   `fixup:instant-reword`: コミットメッセージの書き換え
-   `fixup:instant-amend`: 上記2つを同時に実行
    -   今回の動画に示した例ならこれで一発

生のgitコマンドでやろうとすると、以下のようにそこそこ煩雑な操作です。
まずは`git commit --fixup`や`git rebase --interactive`を覚えるべし......という気持ちもありつつ、生ではinstant感を得られませんね。

1.  `git add`で修正対象のコミットに含める差分をstagingしておく
2.  `git log`で修正対象のコミットを特定する
3.  `git commit --fixup {commit}`で指定したコミットを修正するためのコミットを積む
4.  `git -c sequence.editor=true rebase --interactive --autostash --autosquash --quiet {commit}~`で修正対象のコミットに修正内容のコミットを混ぜつつ、以降のコミットを積み直す

# Tips

## マッピングでやりたい

Ginのアクションは実際には`<Plug>(gin-action-fixup:instant-fixup)`などといったマッピングで定義されています。
頻繁に使うアクションは以下のようにバッファローカルなマッピングを定義すると便利かもしれません。

``` vim
nnoremap <buffer> if <Plug>(gin-action-fixup:instant-fixup)
nnoremap <buffer> ir <Plug>(gin-action-fixup:instant-reword)
```

`:GinLog`で表示しているコミットログは`set nomodifiable`されているため、編集できません。
従って`i`でインサートモードに入ることもないので、`if`や`ir`をinstant fixupやinstant rewordの略称として用いるのはそれなりに合理的だと思います。

## Fuzzy Finderでやりたい

Ginのアクションがマッピングであることは先にも述べた通りです。従ってキーマップをfuzzy findして実行するようなプラグインを利用すると、目的のactionを探しやすくなります。
たとえば以下のようにすると、`a`で本来はGinが実装しているアクション選択モードに入るところを、Telescopeによるアクション選択に差し替えられます。

``` lua
vim.api.nvim_create_autocmd("BufReadCmd", {
  group = vim.api.nvim_create_augroup("gin-custom", {}),
    pattern = "ginlog://*" ,
    callback = function(ctx)
      vim.keymap.set("n", "a", function()
        require("telescope.builtin").keymaps({ default_text = "gin-action " })
      end, { buffer = ctx.buf })
  end,
})
```

**ENJOY!!!**
