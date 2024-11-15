---
title: gh searchでOSS貢献を振り替える
author: atusy
date: '2024-06-03'
slug: gh-search-merged-prs
categories:
  - fish
tags: []
output:
  'blogdown::html_page':
    md_extensions: +east_asian_line_breaks+task_lists
highlightjs:
  - bash
  - json
---


`gh`コマンド、ベンリですね。

こんな感じで、公開レポジトリに作ったPRの内、マージされたものを一発で集計できちゃいます。

今のところ、59レポジトリに167PRをマージしてもらったみたいです。

``` bash
gh search prs \
  --json repository \
  --jq '{ "merged": . | length, "repos": . | map(.repository.nameWithOwner) | unique | length }' \
  --author atusy --visibility public --limit 1000 \
  -- is:merged -owner:atusy
```

``` json
{
  "merged": 167,
  "repos": 59
}
```

`--limit 1000`を指定して、できるだけ沢山の結果を取得していますが、1000PR以上マージされてる偉人には無力。
今のところペジネーションに関するオプションがないのでコントリビューションチャンスっぽい。

**ENJOY!**
