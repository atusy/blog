---
title: telescope.nvimによるjumplistをちょっと便利にするテク
author: atusy
date: '2023-12-12'
slug: telescope-jump-list
categories: [Tech]
tags: []
output:
  blogdown::html_page:
    md_extensions: +east_asian_line_breaks+task_lists
highlightjs: [lua]
---

Vimアドベントカレンダー12/10の記事です。
昨日の記事は以下の2本でした。

-   Omochiceさんによる「[使っているvimプラグインの棚卸し(2023冬)](https://zenn.dev/vim_jp/articles/4fa91c21-fffc-4a74-9444-b06658b194b3)」
-   KaitoMuraokaさんによる「初心者向けに何か」（2023/12/23 9:54時点で未投稿）

[Telescope](https://github.com/nvim-telescope/telescope.nvim/)はNeovimにおけるFuzzy Finderのデファクトの座を勝ち取っていると思います。
便利な一方、痒いところに手を出すと途端に難解でundocumentedなAPIに手を出す羽目になります......。

ということで、[Telescope](https://github.com/nvim-telescope/telescope.nvim/)を使ったjumplistをちょっと便利にする小技を紹介します。

Jumplistは文字通り、Vim/Neovim上でjumpした履歴をもっています。
`<C-O>`で直前の履歴へ、`<C-I>`で直後の履歴へ飛べます。

基本はこれらで十分ですが、定義ジャンプであちこち飛んだ後など、特定の場所に戻りたいがどの程度前かわからない場合にFuzzy Finderが輝きます。
しかし、`:Telescope jumplist`実行時はジャンプリスト上の最後の履歴にカーソルがあっており、現在位置との相対的関係がわかりません。

以下のように、現在のカーソル位置がジャンプリストの何番目にあるか判断し、そこにカーソルを動かすハックを仕込んでおくと便利です。

``` lua
vim.keymap.set("n", "<space>j", function()
  local jumplist = vim.fn.getjumplist()
  require("telescope.builtin").jumplist({
    on_complete = {
      function(self)
        -- select current
        local n = #jumplist[1]
        if n ~= jumplist[2] then
          self:move_selection(jumplist[2] - #jumplist[1] + 1)
        end
      end,
    },
  })
end)
```

TelescopeのUI展開時のカーソル位置から、必要な場所への相対値を探って`move_selection()`するなかなかのHACK。
ほんとはUIに表示されている候補を総当たりして、妥当な場所に`set_selection()`する方がよさそうな気がするのですが、例によってAPIの難解さに破れました。
ここをなんとかできたら本家にPRしたいところ。

**ENJOY**
