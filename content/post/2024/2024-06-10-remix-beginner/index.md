---
title: Remixでフロントエンド入門してみた
author: atusy
date: '2024-06-03'
slug: remix-beginner
categories: [Tech]
tags: [frontend, remix]
output:
  'blogdown::html_page':
    md_extensions: +east_asian_line_breaks+task_lists
highlightjs:
  - typescript
---


ぼちぼちフロントエンドなるもんもやってみたいなーと思い、[Remix](https://remix.run)に入門してみました。

フロントエンドの経験は、仕事でちょっとVue2を触ったことがあるのと、3年ほど前に[React](https://react.dev/)のチュートリアルをやったことがあるくらい。

特に拘りはなく、同僚がおすすめしてた[Remix](https://remix.run)に手を出してみることにしました。

[Remix Tutorial](https://remix.run/docs/en/main/start/tutorial)は連絡先管理システムを改善していく形式で、雰囲気を掴むにはとてもいい感じでした。

所要時間は30分と想定されてますが、しっかり理解しながら進めるとなると1、2時間はかかるんじゃないかな......？と思いました。

チュートリアルを終えて2日もあれば[Rのヘルプ検索システム](https://helpr.atusy.net)なんか作れちゃうあたり、よくできていると思いますし、良い時代ですね。

`loader`やら`action`やら知らない概念が出てきましたが、データ管理の流れが分かりやすくてよかった感じします。

-   `loader`はURLに応じたデータ読み込みを行う
    -   クエリパラメータを更新した時とかも使える
-   `action`はルーティング（ページ移動）やデータの更新を行う
    -   データを作る
        -   空の連絡先の作成
    -   ユーザーがフォームから送信した内容を反映し、ページを移動する
        -   連絡先をの編集画面で結果を保存し、閲覧画面に移動する
        -   連絡先の閲覧画面で連絡先を削除し、トップ画面に移動する

[Remix](https://remix.run)はSSR（サーバーサイドレンダリング）を基本としているのですが、SPAにも対応しています。
せっかくなので、SPA化もしてみたのですが、`loader`や`action`を[React](https://react.dev/)の`useState`で置き換えていくことになり、依存関係の記述に結構な苦労をしました。

ちなみにSPA化はチュートリアルの内容そのものでやったわけではないです。
先ほども軽く触れた、Rのヘルプ検索システムをSSRで実装してからSPA化しました。

<https://helpr.atusy.net>

Rをブラウザ上で動かす[WebR](https://docs.r-wasm.org/webr/latest/)を使ってWebアプリを作ってみたいというのがフロントエンドに手を出してみた理由なのでした。
実は同じ目的のWebアプリをShinyで作ったこともあるのですが、デプロイ先が<https://shinyapps.io>に縛られる点や、あいまい検索機能を自分でフルスクラッチする必要があったことに辛さを感じていました。
SPA + WebRならnodeやRを動かすサーバーが不要なので、Cloudflare Pagesなどにもデプロイできていいですね。
あいまい検索も[fzf-for-js](https://github.com/ajitid/fzf-for-js)が使えます。

Rのヘルプ検索システムについては詳しくはまた別の記事で語ろうと思います。

**ENJOY!**
