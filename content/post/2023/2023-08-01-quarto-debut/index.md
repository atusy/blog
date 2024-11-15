---
title: Hello, Quarto
date: "2023-08-01"
format: hugo-md
jupyter: python3
---

本ブログはずっと[blogdown](https://bookdown.org/yihui/blogdown/)を使って書いてきましたが、心機一転[quarto](https://quarto.org)で書いてみることにします。

といっても[blogdown](https://bookdown.org/yihui/blogdown/)ユーザーであれば移行に特に苦労はなさそうです。

blogdownはHugoを使ってページを構築するので、quartoとhugoの組み合わせ方を調べ、合わせればOK。

> https://quarto.org/docs/output-formats/hugo.html

実質的には、config.tomlファイルを4行加筆・修正するだけでいけました。

> https://github.com/atusy/blog/commit/411e146ffdcd099a43865ed57ec1ff2997413e2f

RStudioから執筆するとどんな使い心地になるか気になりますね。

現時点で、[blogdown](https://bookdown.org/yihui/blogdown/)が直接[quarto](https://quarto.org)をサポートしてはいませんが、以下の流れで[blogdown](https://bookdown.org/yihui/blogdown/)の便利さも享受しながら記事作成ができそうです。

-   Preview用にサーバーを起動しておく
    -   `blogdown::serve_site()`
-   記事を作成する
    -   `blogdown::new_post("記事のタイトル", ext = "qmd")`を実行すると`content/post/2023-08-01-記事のタイトル/index.qmd`のようなファイルが作成される。`ext`引数を省略するには、既定値を`options(blogdown.ext = "qmd")`で変えておく。
-   記事を書く
-   記事を出力する (Ctrl+Shift+K)
