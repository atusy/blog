---
title: fish使い始めた
author: atusy
date: '2024-05-27'
slug: fish
categories: [fish]
tags: []
output:
  'blogdown::html_page':
    md_extensions: +east_asian_line_breaks+task_lists
---


長く、Zshを使っていましたが、Fishに移行しました。

ノープラグインでOKなくらい高機能で工夫せずとも20msで起動するのは快適でいいです。
ネット上のコマンドをコピペした時もそんなに込まらなさそう。

もう少し詳しく、移行に値するなと思った理由を列挙すると以下の通り。

-   今時のFishはインタラクティブシェルとして使うに困らないくらいBash/Zshっぽい書き方に対応してる
    -   対応しているものの例
        -   `export ENVVAR=hoge`
        -   `ENVVAR=hoge cmd`
        -   `true && echo foo || echo bar`
        -   `echo $( echo hi )`
    -   個人的に欲しいけどないものの例
        -   `cat <( echo hello )`はFishでは`cat ( echo hello | psub )`
-   Zshプラグインをいくつか入れてましたが、十分置き換え可能と判断できた
-   `setopt`やら`zstyle`やら勉強しなくてもデフォで良い感じに動く
-   ノープラグインで小さな設定でも十分動くおかげで起動が高速
    -   20msで起動してる

    -   abbrやaliasを除くと、`fish.config`は実質以下の3行

        ``` fish
        mise activate fish | source
        direnv hook fish | source
        zoxide init fish --no-cmd | source
        ```

入れていたZshプラグインは以下のような感じで、Fishに移行可能と判断しました。

-   fishの組込み機能で代替可能
    -   <https://github.com/zdharma-continuum/fast-syntax-highlighting>
        -   シンタックスハイライト
        -   fishはデフォで対応
    -   <https://github.com/zsh-users/zsh-completions>
        -   Tab補完強化
        -   fishはデフォでそこそこ強い
    -   <https://github.com/zsh-users/zsh-autosuggestions>
        -   履歴からの補完
        -   fishはデフォで対応
    -   <https://github.com/woefe/git-prompt.zsh>
        -   プロンプトにGitのブランチとか表示
        -   同期的でよければ、fishはデフォで対応
    -   <https://github.com/junegunn/fzf>
        -   あいまい検索系の色んな機能
        -   個人的にはコマンド履歴の検索（Ctrl-R）を使っていたが、あいまい検索不要ならfishの組込み機能で十分
    -   <https://github.com/yuki-yano/zeno.zsh>
        -   Abbreviation
        -   fishはデフォで対応
-   自分で簡単に実装可能
    -   <https://github.com/jonmosco/kube-ps1>
        -   プロンプトにKubernetesのクラスタとか表示
-   頑張ればどうにでもなる
    -   <https://github.com/atusy/gh-fzf>
        -   ghコマンドとfzfコマンドを組み合わせて便利にするやつ
-   とりあえずなくても生きてける
    -   <https://github.com/atusy/zsh-nvrepl>
        -   zshをNeovimのREPLっぽくするやつ
        -   Neovimの`:term`で起動したzshの中で`:echo expand("%")`とかすると、Neovimで評価した結果を表示する
