---
title: denops製VimプラグインでDenoのバージョンとキャッシュ位置を固定する
author: atusy
date: '2023-12-10'
slug: denops-cache
categories: [Vim, Neovim]
tags: [denops.vim]
output:
  blogdown::html_page:
    md_extensions: +east_asian_line_breaks+task_lists
---

Vimアドベントカレンダー12/10の記事です。
昨日の記事は以下の2本でした。

-   nil2さんによる「[Vimのデフォルトキーマップをどのように上書きするか(ノーマルモード)](https://zenn.dev/nil2/articles/802f115673b9ba)」
-   atusyによる「[VimでgfしたらURLをブラウザで開く](https://blog.atusy.net/2023/12/09/gf-open-url/)」

さて本題。

[denops.vim](https://github.com/vim-denops/denops.vim)というプラグイン開発エコシステムがあります。

> denops.vim は JavaScript/TypeScript のランタイムである Deno を利用して Vim/Neovim 双方で動作するプラグインを作るためのエコシステムです。
> https://zenn.dev/lambdalisue/articles/b4a31fba0b1ce95104c9

denops.vim製プラグインは、高速性やJavascript/Typescriptの資産の恩恵による多機能性があり、この記事の執筆を含め、日々ありがたく利用させていただいております。
代表的なところで以下。

-   自動補完プラグイン[ddc.vim](https://github.com/Shougo/ddc.vim)
-   Gitクライアント[gin.vim](https://github.com/lambdalisue/gin.vim)
-   SKK日本語入力プラグイン[skkeleton](https://github.com/vim-skk/skkeleton)

Denoは実行時に必要な依存関係を自動解決してくれます。
これまた便利なのですが、プラグインのインストール直後やDenoのバージョン変更後に、依存解決で数秒待たされるケースがあります。

プラグインの初回インストールはまだ待てるとして、Denoのバージョンを変更するたびにキャッシュに時間をとられるのは体験が悪いです。
Denoのアップデートに限らず、[rtx](https://github.com/jdx/rtx)や[asdf](asdf-vm.com/)、[pkgx](https://pkgx.sh)などを使ってシステム側のDenoのバージョンを一時的に変更するケースはしばしば存在します。

同様の体験をされた方は以下のように、[denops.vim](https://github.com/vim-denops/denops.vim)用のDenoとキャッシュファイルをシステムに左右されないよう固定するといいでしょう。

``` vim
" denops.vim読み込み前に設定
let g:denops#deno = 'path/to/deno/1.38.4/bin/deno'
let g:denops#deno_dir = 'path/to/deno/1.38.4/cache'
```

ちなみに、`g:denops#deno_dir`というグローバル変数は、最近私がPRして取り込んでもらったものです（<https://github.com/vim-denops/denops.vim/pull/295>）。

私の場合は、設定ファイルの中で[denops.vim](https://github.com/vim-denops/denops.vim)用のDenoのバージョンを指定し、存在しなければ自動的にダウンロードするところまで設定してあります。快適。

> https://github.com/atusy/dotfiles/blob/5c3d3d4984712fdb673d6778f8a01d7f9877ceae/dot_config/nvim/lua/plugins/denops/init.lua?plain=1#L5

また、プラグインの初回インストールやDenoの更新に際して発生する待ち時間も減らすべく、独自に並列キャッシュする仕組みも入れてみてます。快速。

> https://github.com/atusy/dotfiles/blob/5c3d3d4984712fdb673d6778f8a01d7f9877ceae/dot_config/nvim/lua/plugins/denops/init.lua?plain=1#L5

ENJOY!
