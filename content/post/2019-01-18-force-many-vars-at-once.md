---
title: 一度に複数の変数を force する
author: ~
date: '2019-01-18'
slug: force-many-vars-at-once
categories: [R]
tags: [force]
---

# 結論 {#concl}

`force(list(a, b, c, ...))` とすればいい．

```{.r}
f <- function(a, b, c, ...) {
  force(list(a, b, c, ...)) # 先に評価したいものから list に入れる
  10
}

f() 
#> Error in force(list(a, b, c, ...)) : argument "a" is missing, with no default

f(stop("a でエラー"))
#> Error in force(list(a, b, c, ...)) : a でエラー

f(a = 1) 
#> Error in force(list(a, b, c, ...)) : argument "b" is missing, with no default

f(a = 1, b = 1)
#> Error in force(list(a, b, c, ...)) : argument "c" is missing, with no default

f(a = 1, c = 1)
#> Error in force(list(a, b, c, ...)) : argument "b" is missing, with no default

# OK
f(a = 1, b = 1, c = 1)
f(a = 1, b = 1, c = 1, d = 1)
```

# 背景 {#bg}

Rでは関数の引数が遅延評価されるため，引数は使わない限り評価されない
(参考: ["Adv. R: Lazy evaluation"](http://adv-r.had.co.nz/Functions.html#lazy-evaluation))．
明示的に使うには `force` 関数を使う．
単に `x` 
だけの行を入れても強制評価できるが，`force` を使うことで開発者の意図を盛り込もう．

```{.r}
# g は x を評価しないためエラーにならない
g <- function(x) 10
g(stop("エラー"))

# h は x を強制評価するためエラーになる
h <- function(x) {
  force(x)
  10
}
h(stop("エラー"))
```

で，複数の変数を `force` するには `force` を繰り返せばいいが，面倒．
以下のように `force` が複数の引数を受け付けてくれる実装だったらよかったのに．
そう考えたところで，強制したい引数のリストを`force` に渡せばよいとの[結論](#concl)を得た．

```.r
force <- function(...) list(...)
```



