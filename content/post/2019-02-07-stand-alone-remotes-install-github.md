---
title: 専用パッケージを導入せず GitHub 上の R パッケージをインストールする
author: ~
date: '2019-02-07'
slug: stand-alone-remotes-install-github
categories: [R]
tags: [remotes]
---

# TL;DR

GitHub上の R パッケージのインストールは以下のようにコマンド一発でできる．
ブランチの指定や `force = TRUE` による強制インストールなどいろいろできる．

- `source("https://install-github.me/username/repo[/subdir][@ref|#pull]")`
    - 1つのパッケージのみインストールする時用．
- `source("https://raw.githubusercontent.com/r-lib/remotes/master/install-github.R")$value(...)`
    - `...` には `rmeotes::instlal_github()` が受け取る引数を指定．
    - 複数のパッケージも指定可能．

# はじめに

一般に GitHub 上のパッケージをインストールするには `remotes::install_github()` を使う．
`devtools::install_github` もあるが，これは `remotes::install_github()` を流用しているに過ぎない．
あと，`devtools` は色んなパッケージに依存していて，依存パッケージを`devtools::install_github` でインストールしようとすると事故ることがある．
たしかそんな話をy氏がしていたはずなんだけれど，私のググル力が足りなかった．
まあ `remotes` を使うのが無難そう．

初めて `remotes` パッケージを使って `tidyverse/tidyverse` をインストールしようとすると，以下のようにコマンドが2つは必要になる．

```{.r}
install.packages("remotes")
remotes::install_github("tidyverse/tidyverse")
```

これは開発者にも利用者にも優しくない．
開発者は書くべきことが増える．
README に「インストールにはコマンドをコピペしてくれ」と書くだけでは足りず，「`remotes` パッケージをインストールしていない場合はまずインストールしてね」なんて注釈も書き足すことになるだろう．
利用者は読むべきことが増えるし，冗長な README はなんとなく閉じたくなる．

それに `remotes` パッケージは CRAN にあるけどもし GitHub からインストールせざるをえなかったらどうするの？
`remotes` をインストールするために `remotes` をインストールしないといけなくてあああああってなるの？
(※勿論．ローカルに落とせばごにょごにょできる)

# 公式からの素敵なお知らせ

`remotes` パッケージの README を読むと，以下のようなコマンドをコピペするだけで GitHub 上の `remotes` をインストールできる
(https://github.com/r-lib/remotes#installation)．

```r
source("https://install-github.me/r-lib/remotes")
```

または

```r
source("https://raw.githubusercontent.com/r-lib/remotes/master/install-github.R")$value("r-lib/remotes")
```

大体の人はこれで満足するかも？

# ちょっと深入りしてみる

ソースコードにアクセスしてみると，どうやらこいつは `remotes::install_github` のラッパーらしい
(https://raw.githubusercontent.com/r-lib/remotes/master/install-github.R)．
つまり，[`?remotes::install_github`](https://remotes.r-lib.org/reference/install_github.html) に載っていることは一通りできてしまう．

例えば， 

1. `username/repo[/subdir][@ref|#pull]` といった記法による
    - サブディレクトリに存在するパッケージのインストール，
    - 特定のブランチやタグからインストール
        - `r-lib/remotes@master`
        - `r-lib/remotes@v2.0.2`
    - 特定のプルリクからインストール
        - `r-lib/reomtes#266`
1. `dependencies = TRUE` により依存パッケージを全てインストール
1. `upgrade = never` で既存パッケージのアップグレードを行わない

など．

https://install-github.me 経由でのインストールでは1番の機能しか利用できない．

# Enjoy!
