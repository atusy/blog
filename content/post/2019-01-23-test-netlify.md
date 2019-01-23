---
title: Netlify に移行
author: ~
date: '2019-01-23'
slug: tokyor73
categories: [Netlify]
tags: []
---

これまで blog を GitHub pages 上で公開してきた．

しかし，以下の点にメリットを感じ，Netlify への移行を決定した．

- ブランチや PR のプレビューができる
- Publish directory を任意に選択できる
    - これまで GitHub pages のビルドに使っていた docs ディレクトリをそのままにできる
        - リダイレクトを設定できそう
        - その内 repository を切り分けて git submodule 化 & archive するといいかも？
- Publish directory をバージョン管理しなくていい
- md ファイルでよければ GitHub の Web ページ上で編集したものをそのままビルドしてくれる
    - Travis CI を使えば GitHub pages でも実現できそう．

最初から Netlify を使う場合は Yi Hui が How to を書いてくれている．\
https://bookdown.org/yihui/blogdown/netlify.html#fn34

# 移行のためにやったこと

1. .gitignore 
    - Publish directory に設定した "netlify" を追加
1. config.toml の編集
    
    ```{.toml}
    baseurl = "https://atusy-blog.netlify.com/"
    publishDir = "netlify"
    ```
    
1. GitHub に push しておく
1. https://www.netlify.com/
    1. GitHub アカウントでログイン
    1. レポジトリの紐付け
        - Publish directory は config.toml の publishDir と同じにする
    1. Deploy に成功しているか確認
    1. Site name の変更
        - デフォルトではランダムなサブドメインが与えられる \
          `random-site-name.netlify.com`
        - `random-site-name` の部分は早いもの勝ち
        - 自前でドメイン持ってればそっちでもいい
