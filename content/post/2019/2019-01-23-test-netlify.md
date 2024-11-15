---
title: GitHub pages から Netlify に移行 + 独自ドメイン化
author: ~
date: '2019-01-23'
slug: test-netlify
categories: [Netlify]
tags: []
---

これまで blog を GitHub pages 上で公開してきたが，思い立って独自ドメインで Netlify に移行した．

移行のメリットは [Yi Hui が語っている](https://bookdown.org/yihui/blogdown/netlify.html#fn34)けれど，以下に自分にとっての理由と手順の概略を書き留めておく．

# Netlify に移行した理由

- ブランチや PR のプレビューができる
- Publish directory を任意に選択できる
    - これまで GitHub pages のビルドに使っていた docs ディレクトリをそのままにできる
        - リダイレクトを設定できそう
        - その内 repository を切り分けて git submodule 化 & archive するといいかも？
- Publish directory をバージョン管理しなくていい
- md ファイルでよければ GitHub の Web ページ上で編集したものをそのままビルドしてくれる
    - Travis CI を使えば Rmd も含めて GitHub pages でビルドできる．しかし，煩雑なので Yi Hui はオススメしていない．

# 独自ドメインにした理由

サービスを切り替えるごとにドメインを変更するのが嫌になったから．
例えばNetlify に移行するとドメインが atusy.github.io から *.netlify.com に変わる．

ドメインは Google domains から購入した．理由は以下の通り．

  - 1400円/年とまあまあ安い
  - WHOIS 代行によるプライバシー保護が無料
  - サブドメインを100個まで作れる
  - 安定してサービスを提供してくれそう

# 移行のためにやったこと

1. .gitignore 
    - Publish directory に設定した "netlify" を追加
1. config.toml の編集
    
    ```{.toml}
    baseurl = "https://atusy-blog.netlify.com/"
    publishDir = "netlify"
    ```
    
1. GitHub に push しておく
1. Netlify の設定
    1. GitHub アカウントでログイン
    1. レポジトリの紐付け
        - Publish directory は config.toml の publishDir と同じにする
    1. Deploy に成功しているか確認
    1. Setting -> Domain management
        1. Site name を atusy-blog.netlify.com に変更
            - デフォルトではランダムなサブドメインが与えられる．サブドメインは早い者勝ち．
        1. Add domain alias で blog.atusy.net を追加
            - `Check DNS configuration` と警告される．警告をクリックすると以下のようなメッセージが出る．
            
            > Point test CNAME record to atusy-blog.netlify.com
            > Log in to the account you have with your DNS provider, and add a CNAME record for test pointing to atusy-blog.netlify.com.
            
            ```
            blog CNAME atusy-blog.netlify.com.
            ```
            
            > If you’ve already done this, allow up to 24 hours for the changes to propagate, or check our documentation for more information.
1. Google domains の設定
    1. DNS -> Custom resource records
        - 先の Netlify での警告を参考に以下の値を入力

        |Name|Type|TTL|Data|
        |:---|:---|:--|:---|
        |blog|CNAME|1h|atusy-blog.netlify.com.|

1. Netlify の設定2
    1. Setting -> Domain management
        - 警告が消えている
        - blog.atusy.net が緑色になっていてクリックすると atusy-blog.netlify.com と同じ内容が表示される．
        - お好みで HTTPS を有効にする．
    
