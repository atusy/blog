---
title: Neovimの端っこで\<C-W\>lとかしたら、WeztermのとなりのPaneに移動する
author: atusy
date: '2024-05-21'
slug: move-nvim-win-or-wezterm-pane
categories: [Tech]
tags: [Neovim, Wezterm]
output:
  'blogdown::html_page':
    md_extensions: +east_asian_line_breaks+task_lists
---


Weztermで区切ったPaneの中でNeovimを操作していると、`<c-w>l`したのに隣に移動できないぞ？という気分になるときがあります。
右隣はNeovimのWindowではなく、WeztermのPaneですね。

世の中にはNeovim内からWeztermのAPIに簡単にアクセスするためのプラグインがあるので、これを使うと簡単にフラストレーションから開放されます。

<https://github.com/willothy/wezterm.nvim>

たとえば`<c-w>l`したら

1.  `wincmd l`を試す
2.  `wincmd l`の前後でWindow IDが変わらなかった場合は、右方向のWezterm Paneへの移動を試す

といった感じですね。

これを全方向に対応させる設定は以下。

``` lua
local directions = { h = "Left", j = "Down", k = "Up", l = "Right" }

local move_nvim_win_or_wezterm_pane = function(hjkl)
  -- 現在のウィンドウIDを取得
  local oldwin = vim.api.nvim_get_current_win()

  -- ウィンドウ移動を試す
  vim.cmd.wincmd(hjkl)

  -- 現在ウィンドウに変化がなければWeztermのPane移動を試す
  if win == vim.api.nvim_get_current_win() then
    require("wezterm").switch_pane.direction(directions[hjkl])
  end
end

for k, _ in pairs(directions) do
  vim.keymap.set("n", "<c-w>" .. k, function()
    move_nvim_win_or_wezterm_pane(k)
  end)
end
```

Atusyはプラグインマネージャーの[lazy.nvim](https://github.com/folke/lazy.nvim)を使って、Weztermの利用状況に合わせたマッピングの有効化とプラグインの遅延読み込みを行っています。

``` lua
-- ~/.config/nvim/lua/plugins/wezterm/init.lua
local directions = { h = "Left", j = "Down", k = "Up", l = "Right" }

local function move_nvim_win_or_wezterm_pane(hjkl)
  local win = vim.api.nvim_get_current_win()
  vim.cmd.wincmd(hjkl)
  if win == vim.api.nvim_get_current_win() then
    require("wezterm").switch_pane.direction(directions[hjkl])
  end
end

return {
  {
    "https://github.com/willothy/wezterm.nvim",
    lazy = true,
    cond = function()
      return vim.env.WEZTERM_PANE ~= nil
    end,
    init = function(p)
      if not p.cond then
        return
      end
      for k, _ in pairs(directions) do
        vim.keymap.set("n", "<c-w>" .. k, function()
          move_nvim_win_or_wezterm_pane(k)
        end)
      end
    end,
  },
}
```
