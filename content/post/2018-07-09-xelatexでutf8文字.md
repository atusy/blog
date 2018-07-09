---
title: xetexでunicode文字
author: ~
date: '2018-07-09'
slug: xelatexでutf8文字
categories: [latex]
tags: [latex, rmd, rmarkdown, unicode]
---

$\LaTeX{}$ で μ や α など特殊文字を直打ちすると、
□になってしまうことがしばしば。

XeTeXを使っている場合は、

`\setmainfont{IPAMincho}`

など、ユニコードに対応したフォントを使うように指定する。

Rmarkdownユーザーの場合、下記の様にyamlを記述すればよい。

```yaml
---
output:
  pdf_document:
    latex_engine: xelatex
header-includes:
- \usepackage{zxjatype}
- \usepackage[ipa]{zxjafont}
- \setmainfont{IPAMincho}
---
```

ちなみに、現在使っている `header-includes` は

```yaml
header-includes:
- \usepackage{bookmark}
- \usepackage{zxjatype}
- \usepackage[ipa]{zxjafont}
- \usepackage[font={scriptsize}]{caption}
- \renewcommand{\thetable}{\arabic{section}.\arabic{table}}
- \setmainfont{IPAMincho}
```

