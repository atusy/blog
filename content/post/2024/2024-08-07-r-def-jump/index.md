---
title: Rで関数定義のジャンプがしょぼいわけ
author: atusy
date: '2024-08-07'
slug: r-def-jumpt
categories: [Tech]
tags: [R]
output:
  'blogdown::html_page':
    md_extensions: +east_asian_line_breaks+task_lists
---


RStudioなどのエディタは、関数の定義ジャンプ機能を備えます。
VSCodeやVimなどのエディタでもLanguage Service Protocol（LSP）の支援により、関数の定義ジャンプが可能です（<https://cran.r-project.org/web/packages/languageserver/index.html>）。

しかし、定義ジャンプの性能はお世事にも良いとは言えません。
たとえば`purrr::map`関数の定義ジャンプを試すと、`purrr::map`関数を定義しているソースファイルを表示するのではなく、以下のように`purrr::map`関数自身が持つ関数定義の表示を行います。

``` r
# Generated from function body. Editing this file has no effect.
function (.x, .f, ..., .progress = FALSE) 
{
    map_("list", .x, .f, ..., .progress = .progress)
}
```

これでは、`print(purrr::map)`するのと変わりません。

``` r
print(purrr::map)
#> function (.x, .f, ..., .progress = FALSE) 
#> {
#>     map_("list", .x, .f, ..., .progress = .progress)
#> }
#> <bytecode: 0x645bfbc8cd80>
#> <environment: namespace:purrr>
```

TypeScriptやGoなどの言語では、定義ジャンプすると、ソースファイルを開きます。
このメリットは大きく2つでしょう。

-   参照した関数定義の周辺コードを確認できる
-   関数定義内にある関数の定義にもジャンプできる
    -   たとえば、`purrr::map`関数内で利用されている`map_`関数の定義を見たくても、Rの定義ジャンプでは不可能です（`purrr:::map_`など、パッケージとの関係性が明示されている場合を除く）

なぜ、Rの定義ジャンプはしょぼいのか？
それは、パッケージのインストール先を見れば分かります。
Rはインストールしたパッケージのソースファイルを保持していないのです。
パッケージインストール時にソースファイルからのインストールを指定してもダメでした（例：`install.packages("poorman", type = "source")`）。

``` r
file.path(.libPaths(), "purrr") |>
  purrr::keep(fs::dir_exists) |>
  purrr::keep_at(1L) |>
  fs::dir_tree()
#> /home/atusy/R/x86_64-pc-linux-gnu-library/4.4/purrr
#> ├── DESCRIPTION
#> ├── INDEX
#> ├── LICENSE
#> ├── Meta
#> │   ├── Rd.rds
#> │   ├── features.rds
#> │   ├── hsearch.rds
#> │   ├── links.rds
#> │   ├── nsInfo.rds
#> │   ├── package.rds
#> │   └── vignette.rds
#> ├── NAMESPACE
#> ├── NEWS.md
#> ├── R
#> │   ├── purrr
#> │   ├── purrr.rdb
#> │   └── purrr.rdx
#> ├── doc
#> │   ├── base.R
#> │   ├── base.Rmd
#> │   ├── base.html
#> │   ├── index.html
#> │   ├── other-langs.Rmd
#> │   └── other-langs.html
#> ├── help
#> │   ├── AnIndex
#> │   ├── aliases.rds
#> │   ├── figures
#> │   │   ├── lifecycle-archived.svg
#> │   │   ├── lifecycle-defunct.svg
#> │   │   ├── lifecycle-deprecated.svg
#> │   │   ├── lifecycle-experimental.svg
#> │   │   ├── lifecycle-maturing.svg
#> │   │   ├── lifecycle-questioning.svg
#> │   │   ├── lifecycle-soft-deprecated.svg
#> │   │   ├── lifecycle-stable.svg
#> │   │   ├── lifecycle-superseded.svg
#> │   │   └── logo.png
#> │   ├── paths.rds
#> │   ├── purrr.rdb
#> │   └── purrr.rdx
#> ├── html
#> │   ├── 00Index.html
#> │   └── R.css
#> └── libs
#>     └── purrr.so
```

Rでは、おそらく、バイトコンパイルによる高速化や、遅延読み込みの最適化を考慮して、パッケージのオブジェクトをバイナリに閉じ込めているのでしょう（`R/purrr.rdx`など）。
ソースファイルを保持しないのは単に不要だからだと思います。

とはいえ、やはり現代的な開発体験を得るには不便ですね。

r-develとかのメーリスで、インストールしたパッケージのソースファイルを保持するオプションの追加を提案してみるべきでしょうか。

**ENJOY!**
