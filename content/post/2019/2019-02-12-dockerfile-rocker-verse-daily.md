---
title: RStudio daily builds な rocker/verse をビルド時間短かめに作る
author: ~
date: '2019-02-12'
slug: dockerfile-rocker-verse-daily
categories: [Tech]
tags: [R, Docker, R-rocker]
---

**※**
**この記事は元々，Rstudio 1.2.x preview版を利用したい人向けの記事でした.** \
**2019-04-08 に Rstudio 1.2.1335 が正式リリースされたので，** \
**daily builds を使いたい人向けに改題しました．**

成果品: https://hub.docker.com/r/atusy/verse-daily

[`rocker/rstudio-daily` の `Dockerfile`](https://github.com/rocker-org/rstudio-daily/blob/master/latest/Dockerfile) の1行目を以下に変更しただけ．

```
FROM docker/verse:latest
```

# Rocker プロジェクトについて

rocker-org は R を Docker で利用するための様々な Dockerfile を提供してくれている．

https://github.com/rocker-org/rocker

https://hub.docker.com/u/rocker

例えば，

| Repository | Description |
|:---------------|:----------------|
| rocker/r-ver | 素の R |
| rocker/rstudio | r-ver に安定板の Rstudio を足したもの |
| rocker/tidyverse | rstudio に tidyverse と devtools パッケージを足したもの |
| rocker/verse | tidyverse に TeX や bookdown などのドキュメントに便利なをパッケージを足したもの |
| rocker/geospatial | tidyverse に地理空間を扱うためのパッケージを足したもの |

とりあえず rocker/verse あたり入れとくと便利かな．

# rocker/verse でも RStudio daily build を使いたい

常に最新の機能を享受したい enthusiast なあなたへ．
`rocker/rstudio` は正式リリースされた RStudio を使用している (2019/4/14現在は1.2.x)．

RStudio daily build を使える Docker イメージは [`rocker/rstudio-daily`](https://hub.docker.com/r/rocker/rstudio-daily) らしいので，こいつを土台にした `verse` を作ろうかと考えた．しかし，以下のように `rocker/rstudio-daily` を土台に，`rocker/tidyverse` と `rocker/verse` の `Dockerfile` コピペしまくる方法は， `rocker/rstudio-daily` のイメージとの差分が大きくビルドに時間がかかるのでイマイチ．

```
FROM rocker/rstudio-daily:latest

# https://hub.docker.com/r/rocker/tidyverse/dockerfile の2行目以降をコピペ

# https://hub.docker.com/r/rocker/verse/dockerfile の2行目以降をコピペ

```

実は `rocker/rstudio-daily` は `rocker/rstudio` を土台に RStudio や pandoc を上書きしている．
同じ要領で， `rocker/verse` を土台に RStudio や pandoc を上書きするのがビルド時間短縮にはよさそう．

# 実装

ついでなので docker hub でイメージの autobuild もしておく．

- GitHub にて
    - GitHub の `rocker-org/rstudio-daily` をフォーク
    - `latest/Dockerfile` を編集
        - `FROM rocker/rstudio:devel` -> `FROM docker/verse:latest`
- docker hub にて
    - `atusy/verse-daily` レポジトリを作成
        - GitHub のレポジトリを紐付け (`atusy/rstudio-daily`)
    - `Configure Automated Builds` -> `BUILD RULES`
        - `Build Context` を `latest` にする
        - `Save and Build` を実行

## 注意

`rocker/tidyverse` や `rocker/verse` の `Dockerfile` に `rocker/rstudio-daily` の `Dockerfile` と競合する部分があると後者が優先されると思う．

