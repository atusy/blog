---
title: CNAME ファイルだけで GitHub pages から301リダイレクトする
author: ~
date: '2019-03-11'
slug: use-cname-to-redirect-from-gh-pages
categories: [GitHub]
tags: [gh-pages]
---

## TL;DR

GitHub pages を利用していたレポジトリに転送先のドメインを記述した [CNAME](https://github.com/atusy/blog/blob/gh-pages/CNAME) ファイルを作成するだけ．

こんな感じにね．

```
blog.atusy.net
```

# 動機 + 方法発見の経緯

ドメインを購入したのと Netlify に以降したのを理由に， atusy.github.io/blog を blog.atusy.net に転送したくなった．

セキュリティ上の理由から `.htaccess` とか `.conf` は使えないけど， Jekyll でごにょごにょしてくれよなという[公式声明](https://help.github.com/en/articles/redirects-on-github-pages)や，「[Github pages で 別サイトへリダイレクトさせる](https://qiita.com/okhiroyuki/items/a7bc638d9f50de977bd1)」を読んで，できるのは分かったけど Jekyllとか用意するの面倒だなと思った．そこで，同記事が参考に公開しているレポジトリ ([okhiroyuki/okhiroyuki.github.io](https://github.com/okhiroyuki/okhiroyuki.github.io)) をフォークして必要なところだけ弄ればいいじゃんと．

気付いたら CNAME しか残ってませんでした （笑）

# 実装から確認まで

## CNAME ファイルの用意

冒頭にも書いた通り，転送先のドメインを記述した [CNAME](https://github.com/atusy/blog/blob/gh-pages/CNAME) ファイルを用意する．

```
blog.atusy.net
```

私は GitHub Pages で使っていたレポジトリをそのまま Netlify に流用しているので，できれば master ブランチとは関係のないところに CNAME を作りたかった．

GitHub Pages は公開ディレクトリとして 

- `master` ブランチのルートディレクトリ
- `master` ブランチの `docs` ディレクトリ
- `gh-pages` ブランチのルートディレクトリ

を選べるので，`gh-pages` ブランチを Orphan ブランチとして作成し，そこに CNAME を置くことにした．

```{.sh}
git checkout --orphan gh-pages
rm * -R
echo "blog.atusy.net" >> CNAME
git add CNAME
git commit -m "CNAME for 301 redirect"
git push origin gh-pages
```

## GitHub Pages の設定欄を確認

custom domain が blog.atusy.net に変わっているはず．

変わっていなければ，`Source` を一度 `None` にして公開し直した方がいいかも？

以下のような警告が発せられるが無視．

> Your site's DNS settings are using a custom subdomain, blog.atusy.net, that's set up as an A record. We recommend you change this to a CNAME record pointing at [YOUR USERNAME].github.io. For more information, see https://help.github.com/articles/setting-up-a-custom-domain-with-github-pages/.

## curl で status を確認

`curl -I http://atusy.github.io/blog` で 

- `HTTP/1.1 301 Moved Permanently` 
- `Location: http://blog.atusy.net` 

を確認できました．

```{.sh}
curl -I http://atusy.github.io/blog
# HTTP/1.1 301 Moved Permanently
# Server: GitHub.com
# Content-Type: text/html
# Location: http://blog.atusy.net
# X-GitHub-Request-Id: 3E06:1044:DAC20C:ED3386:5C85969D
# Content-Length: 178
# Accept-Ranges: bytes
# Date: Sun, 10 Mar 2019 22:58:38 GMT
# Via: 1.1 varnish
# Age: 0
# Connection: keep-alive
# X-Served-By: cache-itm18827-ITM
# X-Cache: MISS
# X-Cache-Hits: 0
# X-Timer: S1552258718.416877,VS0,VE92
# Vary: Accept-Encoding
# X-Fastly-Request-ID: 49f74f393efb559b7f2c521efc59ec142cf4029e
```

## 実際にアクセスしてみる

https://atusy.github.io/blog/2019/03/11/use-cname-to-redirect-from-gh-pages/#実際にアクセスしてみる

は

https://blog.atusy.net/2019/03/11/use-cname-to-redirect-from-gh-pages/#実際にアクセスしてみる

に転送される．

# Enjoy!!
