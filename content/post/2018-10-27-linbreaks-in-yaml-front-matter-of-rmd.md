---
title: | 
  RmarkdwonのYAMLフロントマターで  
  titleとか  
  authorとか  
  改行する
author: ~
date: '2018-10-27'
slug: linbreaks-in-yaml-front-matter-of-rmd
categories: [R]
tags: [Rmd, YAML, R MarkdownでWord文書を作ろう]
---

@niszet0 さん著「R MarkdownでWord文書を作ろう」を読んでます。
Rmdを扱った商業誌にも、同書ほどRmdファイルのYAMLフロントマターの書式を丁寧に書いている本はないのではないだろうか。
使えれば良いというスタンスだったのもあって、YAMLのフロースタイルとか、始めて学びました。
しかし、これだけ詳しく書いてあるのに改行のことに触れられていないな、とふと。

本記事のタイトル「RmarkdwonのYAMLフロントマターでtitleとかauthorとか改行する」も改行していますね。

これ、どうやってやるか、最初悩む人が多いのではないでしょうか。

単純には、 `html_document` なら `<br>` を、`pdf_document` なら `\n` を仕込めばいいのですが、
統一的な方法や、特に `word_document` に通用する方法を知りたい人は多いはず。

で、とりあえずググるわけですが、

- https://www.task-notes.com/entry/20150922/1442890800
- http://d.hatena.ne.jp/shunsuk/20090822/1250937310

など、情報はあるものの、どうもこれでは改行されない。

色々試した結果、

```yaml
---
title: |
  RmarkdwonのYAMLフロントマターで  
  titleとかauthorとか改行するには  
  スペース2つ入れてから、改行して  
  文章を続ける
---
```

といった具合に `:` の後にスペースを空けて `|` を入力。
改行+インデントして、改行したい場所でスペースを二つ「`  `」入れればいいということが分かりました。

もう一つ、改行しているかどうかが分かりやすい方法として

```yaml
---
title: |
  | RmarkdwonのYAMLフロントマターで  
  | titleとかauthorとか改行するには  
  | スペース2つ入れてから、改行して  
  | 文章を続ける
---
```

といった具合に `|` を使いまくる方法があります。

`html_document` や `pdf_document` では、これを使っていました。
しかしこの方法だと、`word_document` ではタイトルが表示されなくなり、
`blogdown` では

> | RmarkdwonのYAMLフロントマターで| titleとか| authorとか| 改行する

という残念なタイトルができあがることを知りました。

Enjoy!! 


ところでさっき気付いたのですが、 `md` ファイルだとシンタックスハイライトが働いて、 `Rmd` だと働かない……。
なぜ……。
