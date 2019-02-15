---
title: git でプレゼン資料を纏めるなら各資料は submodule 化しとくとよさげ
author: ~
date: '2019-02-14'
slug: submodulize-presentations
categories: [git]
tags: [git-submodule]
---

私はプレゼン資料を [atusy/presentation](https://github.com/atusy/presentation) に纏めて公開している．

プレゼンの機会なんて無制限にあるので色々面倒が生じる気がしてきた．

## 資料ごとに git log を分けたい

submodule ならできる

## 振り返る気のない資料は適宜 local から消したい

ディスク容量節約

```{sh}
git submodule deinit [name]
```

## あの時の資料を参照したい

submodule の中で submodule 化しよう．

レポジトリの外を参照せずに済む．
また，参照したい資料のレポジトリの任意時点の commit を submodule にできる．

おかげでリンク切れなどの事故の心配が減る……はず．

## 特定の資料を集めたレポジトリを作りたくなるかも

新しいレポジトリに各資料のレポジトリを submodule として登録するだけ

```{sh}
mkdir hoge
cd hoge
hub create atusy/hoge
git submodule add git@github.com:atusy/a1
git submodule add git@github.com:atusy/a2
git submodule add git@github.com:atusy/a3
git add .
git commit -m "A collection of presentations"
git push origin master
```

