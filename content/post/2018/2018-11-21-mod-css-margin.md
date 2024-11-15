---
title: CSSでヘッダの行間を調整してみた
author: ~
date: '2018-11-21'
slug: mod-css-margin
categories: [css]
tags: []
---

# h1

から

## h2

そして

### h3

までの余白が
詰め詰めで読み難かったので、修正しました。

# 以前はこんな感じで辛かった

<h2 style="margin:0"> h2 </h2>
h2の内容
<h3 style="margin:0"> h3 </h3>
h3の内容
<h2 style="margin:0"> h2 </h2>
h2の内容
<h3 style="margin:0"> h3 </h3>
h3の内容


# 余白であって、行間ではないので、長い見出しを書いても大丈夫です

# やりかた

hugoを使っているので、テーマが保存されているディレクトリの

`static/css/style.css`

を、作業ディレクトリの

`static/css/style.css`

にコピーした上で、下記を追記した。

```css
.blog-post h1 {
  margin: 1.5em 0em 0em;
}

.blog-post h2 {
  margin: .7em 0em 0em;
}

.blog-post h3 {
  margin: .5em 0em 0em;
}
```

