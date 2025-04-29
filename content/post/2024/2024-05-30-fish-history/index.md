---
title: fishでzshのhistoryも参照したい
author: atusy
date: '2024-05-30'
slug: fish-history
categories: [fish]
tags: []
output:
  'blogdown::html_page':
    md_extensions: +east_asian_line_breaks+task_lists
highlightjs:
  - fish
---


先日、[fish使い始めた](https://blog.atusy.net/2024/05/27/fish/)との話をしたところですが、移行にあたり、Zshのコマンド履歴を使えないことが苦痛になりました。

そんな時も、さっと設定できちゃうFishはステキ。
素朴には以下のようにすると、Zshのコマンド履歴（`~/.zsh_history`）と、Fishのコマンド履歴（`history`コマンドの出力）を合体させて、[fzf](https://github.com/junegunn/fzf)で選択すれば両方の履歴を使えます。

`CTRL-R`の検索を自前定義にするならこんな感じ。

``` fish
function search_history
  begin
    history
    cat ~/.zsh_history | tac
  end | fzf --no-sort --exact
end

function set_commandline_from_history
  commandline -r ( search_history )
end

bind \cr set_commandline_from_history
```

ただし、上記の方法では、改行を含む履歴がある場合に、一つの履歴が複数の候補に分割されてしまいます。
[fzf](https://github.com/junegunn/fzf)は`--read0`すると、候補の区切りにNULL文字を利用できるので、以下のように工夫をこらすと、とても良い感じになります。
さらに、入力中のコマンドを初期検索キーワードとして流用すると体験がよくなることでしょう。

``` fish
function search_history
  begin
    # Fishの履歴
    # 候補の境界はNULL文字
    # 全候補の最後に改行が入らないよう、`string collect`で改行を消す
    history --null | string collect

    # Zshの履歴
    if test -f ~/.zsh_history
      # Fishの履歴との境界がNULL文字になるようechoしておく
      echo -n -e '\0'

      # Zshの履歴ファイルの書式を`history`コマンドに合わせるため、
      # 候補の区切りが改行からNULL文字に変換する操作と、候補の順序の反転を実施
      # ただし、単一候補が複数行にまたがる場合は、行末にバックスラッシュがあるので、
      # イイ感じに処理する
      cat ~/.zsh_history \
        | perl -ne 'chomp; if (s/\\\\$//) {print "$_\0"} else {print "$_\n"}' \
        | tac \
        | perl -pe 's/\0/\\\\\n/g' \
        | perl -ne 'chomp; if (s/\\\\$//) {print "$_\n"} else {print "$_\0"}'
    end
  end | fzf --no-sort --exact --read0 $argv[1]
end

function set_commandline_from_history
  # 入力中のコマンドを初期検索キーワードに使う
  set -l cbuf ( commandline -b $buf )

  # 候補を選択した場合のみ、バッファ（入力中のコマンド）を置換する
  # キャンセルした時は元の入力状態が維持される
  if set -l nbuf ( search_history --query=$cbuf ); and test -n $nubf
    commandline -r $nbuf
  end
end

bind \cr set_commandline_from_history
```

Zshの履歴をFishの履歴に変換してもいいですが、今回の方法だと、なにかの拍子でZshを使った時の履歴も再変換することなく検索できていいですね。

**ENJOY!**
