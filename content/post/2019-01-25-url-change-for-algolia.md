---
title: pkgdown で作った Webサイトを引越ししたら algolia/docsearch-configs に設定変更を PR しよう
author: ~
date: '2019-01-25'
slug: url-change-for-algolia
categories: [R]
tags: [pkgdown, algolia]
description: 'Test description'
---

docsearch を利用すると，pkgdown で作ったページの全文検索機能を簡単に設定できる (https://pkgdown.r-lib.org/articles/pkgdown.html#search)．

先日 pkgdown サイトの URL を qntmap.atusy.net に変更したので，algolia も変えなきゃと思って改めて新規申し込みしてしまった．

すると，こうして欲しいのかい？ やっといたよ．
だったら次から設定ファイルを変更して PR してね，と中の人から連絡を貰いました．

https://github.com/algolia/docsearch-configs/commit/b2d4055445621681ef68d32f53abad5cc0b2c71f#diff-a0c611a6796cf5d251aac23a0d48b55f

ありがたや．

それとは別に，sitemap が以下のようにドメイン直後に `//` を使っててよくないから `/` に直せとのお達しも頂いた．

```{.xml}
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://qntmap.atusy.net//index.html</loc>
  </url>
  <!-- 以下略 -->
</urlset>
```

これは `_pkgdown.yml` の `url` フィールドを `/` で終えていたのがよくなかったようだ．

```{.yaml}
url:https://qntmap.atusy.net/
```

ではなく

```{.yaml}
url:https://qntmap.atusy.net
```

にしたら直った．
