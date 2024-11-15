---
title: GitHub pages with Rmarkdown
author: atusy
date: '2018-07-05'
slug: github-pages-with-rmarkdown
categories: [R]
tags: [blogdown]
---

遅蒔きながら、Rのblogdownパッケージを使ってblogを始めてみた。

["Rとblogdownでかんたんにgithub.io上にブログを使ってみよう！！"](https://qiita.com/masato_t/items/7bbfa74f8de0dc06c91c)

を参考にしたのだが、何点かハマったところがあったのでメモ。

- `baseurl = "/"`
- トップページが404の時はもう一度pushしてみる
- 記事の規定拡張子はoptionで指定
    - `option(blogdown.ext = '.Rmd')`
    - 参考URLにある `option(blogdown.Rmd = TRUE)` は過去のもの?

    
    