---
title: プレゼン資料のレポジトリはサブモジュールを纏めたものにしておくといいかも？
author: ~
date: '2019-02-14'
slug: submodulize-presentations
categories: [git]
tags: [git-submodule]
---

私はプレゼン資料を [atusy/presentation](!https://github.com/atusy/presentation) に纏めて公開している．

プレゼンの機会なんて無制限にあるので色々面倒が生じる気がしてきた．

## 資料ごとに git log が分かれていないのはジャマくさい

submodule ならできる

## 振り返る気のない資料は適宜 local から消したい

ディスク容量節約

```
git submodule deinit [name]
```

## 特定のプレゼンだけ集めたレポジトリを作りたくなるかも

```
mkdir hoge
cd hoge
hub create atusy/hoge
git submodule add atusy/a1
git submodule add atusy/a2
git submodule add atusy/a3
git add .
git commit -m "A collection of presentations"
git push origin master
```

