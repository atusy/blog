---
title: R3.5系ではファイル同期ソフトでパッケージを同期しないように
author: ~
date: '2018-07-31'
slug: dont-sync-pkg-r3-5
categories: [R]
tags: [package]
---

タイトル通り、R3.5系ではファイル同期ソフトでパッケージを同期しないようにしましょう。  

同期しておくとある環境にインストールしたパッケージを他の環境でもすぐさま利用できて便利だったのですが……。

これは、R.3.5.0からパッケージをバイトコンパイルしてインストールするようになったことが原因です。  

おかげでパッケージはシステムに最適化され、高速に動きます (3.4系までと比べて)。  

代わりに、複数のPCでインストール済みRパッケージを同期すると、

`'pkg' was installed by an R version with different internals'

というエラーを発してしまいます X(