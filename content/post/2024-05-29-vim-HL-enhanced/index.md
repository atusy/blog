---
title: H/LとPageUp/PageDownを共存させる設定 (submode編)
author: atusy
date: '2024-05-29'
slug: vim-HL-enhanced
categories:
  - vim
tags: []
output:
  'blogdown::html_page':
    md_extensions: +east_asian_line_breaks+task_lists
highlightjs:
  - vim
---


この記事は、[Vim駅伝](https://vim-jp.org/ekiden/)の2024年5月29日の記事です。

22日の記事でH/LとPageUp/PageDownを共存させる設定の紹介がありました。

> https://zenn.dev/vim_jp/articles/20240522_ekiden_better_hl

`H`と`L`は通常では、表示領域内の最初の行や最後の行にカーソルを移動させるコマンドです。
連打しやすい割に、連打する意味がない、惜しい存在ですが、スクロール機能も持たせるのは良いアイデアですね。

というわけで、似たようなことを、疑似サブモードを利用して実現してみました。

以下のマッピングを定義すると、`H`単発でウィンドウ上端へのカーソル移動、連打で`<PageUp>`に変身します。
難読な気もしますが、たった4行で実現できるのが凄いですね。

``` vim
nnoremap H H<Plug>(H)
nnoremap L L<Plug>(L)
nnoremap <Plug>(H)H <PageUp><Plug>(H)
nnoremap <Plug>(L)L <PageDown><Plug>(L)
```

挙動としては以下のような流れ。

-   `H`を入力すると、オリジナルの`H`として動作した後、`<Plug>(H)`を入力した状態になる
-   Vimは、`<Plug>(H)`をprefixに持つマッピングがくるのを一定時間待機する
-   待機中に`H`を入力すると、`<Plug>(H)H`扱いになり、`<PageUp>`した後、もう一度`<Plug>(H)`をprefixとした待機状態になる

なお、`<PageUp>`の直後に`H`を、`<PageDown>`の直後に`Lzb`を仕込んでおくと、カーソル位置が良い感じに調整されると思います。

``` vim
nnoremap H H<Plug>(H)
nnoremap L L<Plug>(L)
nnoremap <Plug>(H)H <PageUp>H<Plug>(H)
nnoremap <Plug>(L)L <PageDown>Lzb<Plug>(L)
```

`<PageUp>H`や`<PageDown>L`をすると、連打中のカーソル位置が常にウィンドウの上端か下端に固定されます。
また、バッファ最終行で`<PageDown>`すると、ウィンドウに表示される内容が最終行だけになってしまいスクロールし過ぎな感じになります。
`<PageDown>Lzb`のように`zb`を含めると、カーソル位置をウィンドウの下端に寄せることができ、情報量が多くて良い感じになります。

**ENJOY**
