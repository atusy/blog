---
title: Vimで無名レジスタでchange/delete/yankした時に、イニシャルに相当するレジスタにも値を入れる
author: atusy
date: '2023-12-17'
slug: vim-easy-to-remember-regnames
categories: [Tech]
tags: [Vim]
output:
  blogdown::html_page:
    md_extensions: +east_asian_line_breaks+task_lists
highlightjs: [vim, lua]
---

Vim Advent Calendar 2023の12/17の記事です。
昨日の記事は以下の通りでした。

-   mattnさんによる「[Vim で SQL を素で編集してるの？](https://zenn.dev/mattn/articles/8716db121781d2)」

Vimのレジスタ、使いこなしてますか？
とっても沢山種類があります。

> [\[Vim問題\] レジスタは全部で何種類？](https://vim.blue/vim-all-register/)

いくらか使っているものがあるものの、特に名前付きレジスタはちっとも使い込なせてません。
だって、`a`から`z`まで、どれをどこに入れたかわからなくなるので、`a`くらいしか使い道がない......。

一方、`ciw`したら使いたかったレジスタ上書きしちゃったじゃん！みたいなできごともしばしばです。
たいていの場合、`"0`にyankした結果が、`"-`に`ciw`した結果が入っているので、なんとでもなるっちゃなるのですが、とっさに思考がついていきません。

というわけで考えました。changeしたらcに、deleteしたらdに、yankしたらyに保存しとけばいいのでは......？と。
単純にマッピングで解決するなら、

``` vim
nnoremap c "cc
xnoremap c "cc
nnoremap d "dd
xnoremap d "dd
nnoremap y "yy
xnoremap y "yy
```

といった具合にマッピングすればOKです。
しかしこの方法では、`"ayy`といった具合に明示的にレジスタを指定できなくなる、無名レジスタが更新されないので`p`が使い物にならない、といった問題があります。

expression mappingを使って、指定しているレジスタ（`v:register`）の中身を見る手もあるでしょうが、すべてにexpression mappingを設定するのも面倒そうです。

実は、`TextYankPost`というイベントは名前と裏腹（？）に、changeやdeleteでレジスタが更新された場合も発火する上に、`v:event`変数に契機となったオペレータやレジスタが登録されるので、便利です。
以下のように、無名レジスタが更新された場合に、使用中のオペレータの種類（c/d/y）の名前を冠するレジスタに内容をコピーできます。
これで、あっちゃあ、yankした内容をchangeで上書きしちゃったよと思った時も、yankだからyレジスタで、`"yp`すればオーケー、まだ慌てる時間じゃない、とスムーズに判断できる......かもしれません。

``` vim
" Vim script
function! UseEasyRegname()
  if v:event.regname ==# ''
    call setreg(v:event.operator, getreg())
  endif
endfunction

augroup UseEasyRegname
  autocmd!
  au TextYankPost * call UseEasyRegname()
augroup END
```

ちなみに上記のVim scriptは以下のLuaスクリプトをChatGPTに変換させてから手直ししたものです。

``` lua
-- Lua
vim.api.nvim_create_autocmd("TextYankPost", {
  group = vim.api.nvim_create_augroup("use-easy-regname", {}),
  callback = function()
    if vim.v.event.regname == "" then
      vim.fn.setreg(vim.v.event.operator, vim.fn.getreg())
    end
  end,
})
```

なお、この方法にも欠点はあります。

-   dレジスタを使うdelete系コマンドは`d`・`D`以外にも`x`や`X`がある
-   cレジスタを使うchange系コマンドは`c`・`C`以外にも`s`や`S`がある

これらのマッピングに大しては強制的にxレジスタやsレジスタを割り当てるのも手でしょう。
Atusyの場合は、以下のようにしています。

-   `x`と`X`は`x`レジスタを使うようにマッピング (`nnoremap x "xx`)
-   `s`と`S`はそもそも別用途にマッピング（元の`s`と`S`は`cl`と`cc`で十分）

**Enjoy**
