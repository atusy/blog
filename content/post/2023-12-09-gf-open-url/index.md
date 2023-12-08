---
title: VimでgfしたらURLをブラウザで開く
author: atusy
date: '2023-12-09'
slug: gf-open-url
categories: [Vim, Neovim]
tags: []
output:
  blogdown::html_page:
    md_extensions: +east_asian_line_breaks+task_lists
---

Vimアドベントカレンダー12/9の記事です。
昨日の記事は以下の2本でした。

-   NI57721さんによる「[長文丸暗記用のVimプラグインを作った話](https://zenn.dev/vim_jp/articles/vim-shakyo-plugin)」
-   yasunori0418さんによる「[ヘルプから始めるddu](https://zenn.dev/vim_jp/articles/0005-search_help_with_ddu)」

# gfはいいぞ

`gf`コマンド、便利ですよね。
ファイル名前の上で`gf`と入力すると、そのファイルをバッファに開いてくれます。

この上位互換に`gF`もあり、`file.txt:30` みたくファイル名に行番号が付いている場合に該当業を開いてくれます。
なので、以下のように`gf`を`gF`にしてしまうのは定番といえます。

``` vim
nnoremap gf gF
```

いきなり脱線しましたが、`:help gf`を見ると、**netrw**プラグインを入れてればURIも開けるよとのこと。何それ便利。

> If the name is a hypertext link, that looks like "type://machine/path", you need the \|netrw\| plugin.

**netrw**はいらないけど、URLくらいは開きたいので、実装してみました。

# マッピングを使う

たぶん、王道です。
カーソル下のURLを見つけて、任意のプログラムで開きます。

これまた `:help gf` を読んで気付いたのですが、`<cfile>`という文字列は、カーソル下にあるファイル名に相当するそうです。
従って`expand('<cfile>')`すると、実際のファイル名（URL）に展開されます。

あとは`'<cfile>'`がURLかどうか判定して動作を切り替えればOK。
Linuxなら`xdg-open`を使うといいでしょう。他は知らん。
Neovim nightly使いなら、`vim.ui.open()`という関数でよしなにできるっぽいです。

``` lua
-- Lua (Neovim向け)
vim.keymap.set("n", "gf", function()
  local cfile = vim.fn.expand("<cfile>")
  if cfile:match("^https?://") then
    -- Neovim nightlyなら `vim.ui.open(cfile)` が便利。
    vim.fn.system({"xdg-open", cfile})
  else
    vim.cmd("normal! gF")
  end
end)
```

``` vim
" Vim script (ChatGPTに翻訳させたものを手直し)
function! OpenFileOrURL()
  let cfile = expand("<cfile>")
  if match(cfile, '^https\?://') >= 0
    call system('xdg-open ' . cfile)
  else
    normal! gF
  endif
endfunction

nnoremap <silent> gf :call OpenFileOrURL()<CR>
```

# 自動コマンドを使う

あるいはこんなものも面白いかもしれません。
特に設定してない状態でURLにカーソルを合わせえて`gf`すると、URLをファイル名とした空のバッファが開きます。
これを逆手にとって、`BufReadCmd`イベントで発火する自動コマンドを登録します。

バッファの開閉という副作用がデメリットですが、`:e https://example.com`などでブラウザが開くようになるのは便利かも？

やることとしては以下の通り。
Luaスクリプトを用意してますが、Vim scriptが必要な人はChatGPTなりなんなりに問い合わせてください。

1.  ファイル名前が`https://`または`http://`で始まることを条件とする
2.  任意のコマンド（ブラウザ）でファイルを開く
3.  空のバッファがゴミになるので、直前のバッファを開きなおし（`e #`）、ゴミバッファを消す
    -   直前のバッファを開きなおして、ゴミバッファを非表示にしておくのがポイントで、これにより、バッファを消したせいでウィンドウが閉じるのをふせげます。

``` lua
vim.api.nvim_create_autocmd("BufReadCmd", {
  desc = "Open browser with gf",
  pattern = { "https://*", "http://*" },
  group = vim.api.nvim_create_augroup("open-browser"),
  callback = function(ctx)
    if vim.ui.open then
      -- Neovim nightlyを使っている場合
      vim.ui.open(ctx.match)
    else
      vim.fn.system({"xdg-open", cfile})
    end
    vim.cmd([[e # | bdelete #]])
  end,
})
```

# ENJOY!

`<cfile>`を知らず、最初に思いついたのが自動コマンドでした。ヘルプ読むのって面白いですね！
