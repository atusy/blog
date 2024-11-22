---
title: gyでVimからクリップボードにヤンクする
author: atusy
date: '2024-03-11'
slug: vim-gy-as-gui-yank
categories: [Vim]
tags: []
output:
  blogdown::html_page:
    md_extensions: +east_asian_line_breaks+task_lists
---

[Vim 駅伝](https://vim-jp.org/ekiden/)の2024/3/11の記事です。

Vim/Neovimで文字列をクリップボードへヤンクする主な方法は大きく二通りあります。

-   都度指定
    -   `"*y`や`"+y`といった具合にヤンクする時にクリップボードを使うよう、明示的にレジスタを指定する
-   自動同期
    -   `set clipboard+=unnamedplus`（または`unnamed`）しておき、レジスタを指定せずにヤンクした内容を自動的にクリップボードに同期する

詳しくは以下の記事をご参照ください。

> [Hack #126: クリップボードを利用する](https://vim-jp.org/vim-users-jp/2010/02/21/Hack-126.html)

自動同期は一見便利そうですが、Vim内の文字列をVim外へ貼りつけたいケースはヤンクする頻度からするとごく僅かです。
また、`'clipboard'`オプションは、削除（`d`・`x`）や編集（`c`や`s`）などを実行した時もクリップボードを上書きするため、やりすぎ感があります。
Vimから消した文字列を別所に貼りつけたいことってありますか......？
クリップボードの履歴を使う人は、履歴汚染も気になるでしょう。

一方で都度指定するには`"+`がそこそこ入力しにくい問題があります。

そこで、atusyは以下のように、`gy`をGUI-yankくらいのつもりで、クリップボードにヤンクするためのマッピングに割り当てています。
たとえば`gyiW`すると、非空白文字列の連続する範囲をクリップボードにヤンクできるわけです。

``` vim
noremap gy "+y
```

`g`から始まるマッピングは大部分がデフォルト定義を持ちますが、偶然にも`gy`は空いているので、遠慮なく使えますね。

もし、どうしても自動化したいが、削除や編集ではクリップボードを上書きしてほしくない場合は、以下の記事を参考にしてみてください。
`TextYankPost`イベントではレジスタを変更した操作の種別を検出できるので、ヤンク（`y`）によって無名レジスタが変更された場合に、その内容をクリップボードに同期するといった設定も可能なはずです（未検証）。
これなら`'clipboard'`オプションも不要ですね。

> [Vimで無名レジスタでchange/delete/yankした時に、イニシャルに相当するレジスタにも値を入れる](https://blog.atusy.net/2023/12/17/vim-easy-to-remember-regnames/)

**ENJOY**