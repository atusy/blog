---
output:
  blogdown::html_page:
    toc: true
title: Hugo (blogdown) で MathJax
author: ~
date: '2019-05-09 18:00:00'
slug: how2mathjax
categories: [Tech]
tags: [R, R-blogdown, Hugo, MathJax, LaTeX]
math: true
aliases:
  - /2018/07/28/how2mathjax/
summary: Hugo (blogdown) で MathJax を利用する方法を紹介．ただし，2019-05-09 以降は KaTeX を採用しているため，数式のレンダリングは KaTeX によるもの．
---

- 2018-07-28 公開\\
- 2019-05-09 
    - 「blogdownでMathJax」から「Hugo (blogdown) で MathJax」に改題
    - KaTeX 採用に伴い，下記の数式は KaTeX がレンダリングしている

# MathJaxとは？

MathJaxを利用すると、$\TeX$ 記法を用いて数式を表現できる。

ブロックにするには

```tex
$$
\LaTeX{}
$$
```

と入力すると

$$
\LaTeX{}
$$

となる。

インラインでも `$\LaTeX{}$` とすると、 $\LaTeX{}$ となる。 

ブロックでは `$$` から成る2行の間に、 インラインでは同じ行の `$` 2字の間に $\TeX{}$ 記法を用いることがポイントだ。

# blogdownではインラインでMathJaxが使えない……？

しかし、blogdownのデフォルトテーマ (Hugo Lithium) ではインラインの数式を表現できなかった。

`mathjax blogdown` で検索して、

- [Yi Hui によるドキュメント](https://bookdown.org/yihui/blogdown/templates.html) や、 
- [ぞうさんの記事 ( blogdownで数式がうまく表示されない場合の対処)](https://qiita.com/kazutan/items/fd76b54587e1787eb201)

を参考にするも効果なし。

結局 `mathjax 使い方` で検索して、

- [くろきげんさんの記事(MathJaxの使い方)](http://genkuroki.web.fc2.com/)

も参考にしたところ、インラインで使うにはちょっとコードに工夫がいるらしいことが判明。

# 解決方法 {#solution}

`./themes/hugo-lithium/layouts/partials/footer_mathjax.html`

を下記に書き換える。

```html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({ tex2jax: { inlineMath: [['$','$'], ["\\(","\\)"]] } });
</script>
<script async
src="//cdn.bootcss.com/mathjax/2.7.1/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
```

1-3行目はがインラインでmathjaxを動かすために必要なコード。

4-6行目は利用MするathJaxのバージョンを指定する部分。
くろき氏の記事では2.7.0だったがYi Hui氏の記事では2.7.1だったので、後者にしてみた。

くろき氏のコードでは最終行が下記になっているが、なくても動くっぽい？

`<meta http-equiv="X-UA-Compatible" CONTENT="IE=EmulateIE7" />`



