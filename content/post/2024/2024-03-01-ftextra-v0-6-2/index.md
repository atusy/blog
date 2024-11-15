---
title: ftExtra v0.6.2をリリースしました
author: atusy
date: '2024-03-01'
slug: ftextra-v0-6-2
categories: [R]
tags: []
output:
  blogdown::html_page:
    md_extensions: +east_asian_line_breaks+task_lists
---

<link href="index_files/libs/tabwid-1.1.3/tabwid.css" rel="stylesheet" />
<script src="index_files/libs/tabwid-1.1.3/tabwid.js"></script>


[ftExtra](https://ftextra.atusy.net/) v0.6.2をリリースしました。

[flextable](https://ardata-fr.github.io/flextable-book/)パッケージを使って表組みする時に、セル内のマークダウンを処理できる `ftExtra::colformat_md()` がウリです。

``` r
data.frame(
  x = c("**bold**", "*italic*"),
  y = c("^superscript^", "~subscript~"),
  z = c("***~ft~^Extra^** is*", "*Cool*"),
  stringsAsFactors = FALSE
) |>
  flextable::flextable() |>
  ftExtra::colformat_md()
```

<div class="tabwid"><style>.cl-9f195392{}.cl-9f13596a{font-family:'DejaVu Sans';font-size:11pt;font-weight:normal;font-style:normal;text-decoration:none;color:rgba(0, 0, 0, 1.00);background-color:transparent;}.cl-9f135974{font-family:'DejaVu Sans';font-size:11pt;font-weight:bold;font-style:normal;text-decoration:none;color:rgba(0, 0, 0, 1.00);background-color:transparent;}.cl-9f13597e{font-family:'DejaVu Sans';font-size:6.6pt;font-weight:normal;font-style:normal;text-decoration:none;color:rgba(0, 0, 0, 1.00);background-color:transparent;position: relative;bottom:3.3pt;}.cl-9f13597f{font-family:'DejaVu Sans';font-size:6.6pt;font-weight:bold;font-style:italic;text-decoration:none;color:rgba(0, 0, 0, 1.00);background-color:transparent;position: relative;top:3.3pt;}.cl-9f135988{font-family:'DejaVu Sans';font-size:6.6pt;font-weight:bold;font-style:italic;text-decoration:none;color:rgba(0, 0, 0, 1.00);background-color:transparent;position: relative;bottom:3.3pt;}.cl-9f135989{font-family:'DejaVu Sans';font-size:11pt;font-weight:normal;font-style:italic;text-decoration:none;color:rgba(0, 0, 0, 1.00);background-color:transparent;}.cl-9f135992{font-family:'DejaVu Sans';font-size:6.6pt;font-weight:normal;font-style:normal;text-decoration:none;color:rgba(0, 0, 0, 1.00);background-color:transparent;position: relative;top:3.3pt;}.cl-9f168324{margin:0;text-align:left;border-bottom: 0 solid rgba(0, 0, 0, 1.00);border-top: 0 solid rgba(0, 0, 0, 1.00);border-left: 0 solid rgba(0, 0, 0, 1.00);border-right: 0 solid rgba(0, 0, 0, 1.00);padding-bottom:5pt;padding-top:5pt;padding-left:5pt;padding-right:5pt;line-height: 1;background-color:transparent;}.cl-9f1690b2{width:0.75in;background-color:transparent;vertical-align: middle;border-bottom: 1.5pt solid rgba(102, 102, 102, 1.00);border-top: 1.5pt solid rgba(102, 102, 102, 1.00);border-left: 0 solid rgba(0, 0, 0, 1.00);border-right: 0 solid rgba(0, 0, 0, 1.00);margin-bottom:0;margin-top:0;margin-left:0;margin-right:0;}.cl-9f1690bc{width:0.75in;background-color:transparent;vertical-align: middle;border-bottom: 0 solid rgba(0, 0, 0, 1.00);border-top: 0 solid rgba(0, 0, 0, 1.00);border-left: 0 solid rgba(0, 0, 0, 1.00);border-right: 0 solid rgba(0, 0, 0, 1.00);margin-bottom:0;margin-top:0;margin-left:0;margin-right:0;}.cl-9f1690bd{width:0.75in;background-color:transparent;vertical-align: middle;border-bottom: 1.5pt solid rgba(102, 102, 102, 1.00);border-top: 0 solid rgba(0, 0, 0, 1.00);border-left: 0 solid rgba(0, 0, 0, 1.00);border-right: 0 solid rgba(0, 0, 0, 1.00);margin-bottom:0;margin-top:0;margin-left:0;margin-right:0;}</style><table data-quarto-disable-processing='true' class='cl-9f195392'><thead><tr style="overflow-wrap:break-word;"><th class="cl-9f1690b2"><p class="cl-9f168324"><span class="cl-9f13596a">x</span></p></th><th class="cl-9f1690b2"><p class="cl-9f168324"><span class="cl-9f13596a">y</span></p></th><th class="cl-9f1690b2"><p class="cl-9f168324"><span class="cl-9f13596a">z</span></p></th></tr></thead><tbody><tr style="overflow-wrap:break-word;"><td class="cl-9f1690bc"><p class="cl-9f168324"><span class="cl-9f135974">bold</span></p></td><td class="cl-9f1690bc"><p class="cl-9f168324"><span class="cl-9f13597e">superscript</span></p></td><td class="cl-9f1690bc"><p class="cl-9f168324"><span class="cl-9f13597f">ft</span><span class="cl-9f135988">Extra</span><span class="cl-9f135989"> </span><span class="cl-9f135989">is</span></p></td></tr><tr style="overflow-wrap:break-word;"><td class="cl-9f1690bd"><p class="cl-9f168324"><span class="cl-9f135989">italic</span></p></td><td class="cl-9f1690bd"><p class="cl-9f168324"><span class="cl-9f135992">subscript</span></p></td><td class="cl-9f1690bd"><p class="cl-9f168324"><span class="cl-9f135989">Cool</span></p></td></tr></tbody></table></div>

今回はマークダウン内でHorizontalRule（水平線）を使った場合に、エラーが発生するというバグの修正でした。
そもそも表の中で水平線を使いたいシーンがあるか分かりませんが、そもそもflextableが水平線に対応していないこともあり、どんな記法を使っても`---`に置換する処理となっています。
これは、Pandocでマークダウンをパースした瞬間に元の文字列の情報が失われ、どんな記法で書かれたか分からなくなるためです。

``` r
data.frame(x = c("---", "***", "_ _ _")) |>
  flextable::flextable() |>
  ftExtra::colformat_md()
```

<div class="tabwid"><style>.cl-9f5d308a{}.cl-9f4e1000{font-family:'DejaVu Sans';font-size:11pt;font-weight:normal;font-style:normal;text-decoration:none;color:rgba(0, 0, 0, 1.00);background-color:transparent;}.cl-9f504b18{margin:0;text-align:left;border-bottom: 0 solid rgba(0, 0, 0, 1.00);border-top: 0 solid rgba(0, 0, 0, 1.00);border-left: 0 solid rgba(0, 0, 0, 1.00);border-right: 0 solid rgba(0, 0, 0, 1.00);padding-bottom:5pt;padding-top:5pt;padding-left:5pt;padding-right:5pt;line-height: 1;background-color:transparent;}.cl-9f5056d0{width:0.75in;background-color:transparent;vertical-align: middle;border-bottom: 1.5pt solid rgba(102, 102, 102, 1.00);border-top: 1.5pt solid rgba(102, 102, 102, 1.00);border-left: 0 solid rgba(0, 0, 0, 1.00);border-right: 0 solid rgba(0, 0, 0, 1.00);margin-bottom:0;margin-top:0;margin-left:0;margin-right:0;}.cl-9f5056d1{width:0.75in;background-color:transparent;vertical-align: middle;border-bottom: 0 solid rgba(0, 0, 0, 1.00);border-top: 0 solid rgba(0, 0, 0, 1.00);border-left: 0 solid rgba(0, 0, 0, 1.00);border-right: 0 solid rgba(0, 0, 0, 1.00);margin-bottom:0;margin-top:0;margin-left:0;margin-right:0;}.cl-9f5056da{width:0.75in;background-color:transparent;vertical-align: middle;border-bottom: 1.5pt solid rgba(102, 102, 102, 1.00);border-top: 0 solid rgba(0, 0, 0, 1.00);border-left: 0 solid rgba(0, 0, 0, 1.00);border-right: 0 solid rgba(0, 0, 0, 1.00);margin-bottom:0;margin-top:0;margin-left:0;margin-right:0;}</style><table data-quarto-disable-processing='true' class='cl-9f5d308a'><thead><tr style="overflow-wrap:break-word;"><th class="cl-9f5056d0"><p class="cl-9f504b18"><span class="cl-9f4e1000">x</span></p></th></tr></thead><tbody><tr style="overflow-wrap:break-word;"><td class="cl-9f5056d1"><p class="cl-9f504b18"><span class="cl-9f4e1000">---</span></p></td></tr><tr style="overflow-wrap:break-word;"><td class="cl-9f5056d1"><p class="cl-9f504b18"><span class="cl-9f4e1000">---</span></p></td></tr><tr style="overflow-wrap:break-word;"><td class="cl-9f5056da"><p class="cl-9f504b18"><span class="cl-9f4e1000">---</span></p></td></tr></tbody></table></div>

前回が9月なのでおよそ半年ぶりのリリースですね。
データサイエンスから離れて久しく、凝った表組みや文書作成をする機会も乏しいので私が利用するシーンは全然ありません。
その割にはまめにIssue対応できているのではないかなと自画自賛しています。

[ftExtra](https://ftextra.atusy.net/)はナゾの勢いでかきなぐったパッケージなので、たまにメンテするには処理の理解が追い付かない部分があります。
その内書き直したいなあという気持ちと、それなら[gt](https://gt.rstudio.com/)向けの処理を実装するとかの方が面白いのではという気持ちで揺れてますね。
[gt](https://gt.rstudio.com/)はcommonmarkに対応していますが、Pandoc's Markdownに対応していないので、R MarkdownやQuartoとの相性が抜群とは言えない......と思ってます。

ENJOY!
