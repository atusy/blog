---
title: Antergos導入
author: ~
date: '2018-10-11'
slug: hello-antergosmd
categories: [Arch]
tags: [Linux]
---

自宅用PCにAntergosを導入しました．

ppaを足すも.debや.tar.gzを落とすもなんかかったるくなってAURが楽しそうなArchlinux系列を試すことにしました．

Antergosにした理由は，デスクトップ環境として慣れ親しんだCinnamonを簡単に導入できるからです．

導入は公式の提供する手順通りに進めれば簡単です．

以下は日本語入力環境をセットアップするまでの備忘録です．

# OSインストール

localeにはen_us.utf-8を選び，初期に追加インストールできるパッケージとして，Bluetooth, Firefox, LibreOffice, Printing Support, ssh, ufwを追加しました．

# Keyboard設定

Caps LockをCtrl化

# guakeの導入

どこでもterminalですね．

```sh
sudo pacman -S guake
```

でインストール

`Guake properties` から，

- Startup時のPopup通知無効化
- ログイン時に自動起動
- サイズを横50%，縦70%程度
- 位置を画面左側

に設定しました．

# 日本語環境導入

日本語フォントと日本語入力環境を導入します([参考](https://qiita.com/l7u7ch/items/f88cda88ab95176e870f))

私はCinnamonとfcitx-skkを使うので，上記参考リンクとは若干手順が違います．

フォントにはとりあえずipafontを入れますが，ここはお好みで．

## パッケージ導入 + スタートアップスクリプト作成

```sh
sudo pacman -S otf-ipafont fcitx fcitx-configtool fcitx-gtk2 fcitx-gtk3 fcitx-qt4 fcitx-qt5 fcitx-skk skk-jisyo
echo "export GTK_IM_MODULE=fcitx" > ~/.xprofile
echo "export QT_IM_MODULE=fcitx" >> ~/.xprofile
echo "export XMODIFIERS=@im=fcitx" >> ~/.xprofile
```

## システムとFirefoxのフォントを設定

- `System Settings` -> `Fonts` -> Monospace font以外をIPAPGothic Regularに．
- `Firefox` -> `prereference` -> `Fonts & Colors` -> `Default font` を IPAPGothic Regularに．

## fcitxの設定

- 再ログイン
- `System Tray`上の`fcitx`を右クリック-> `configure`
- `Input Method`右下の`+` -> `Only Show Current Language`のチェックを外す -> `skk`を選択 -> `OK`
- `Input Method`の`Keyboard - English (US)`を選択->右下の`-`を押す
- `Input Method`に追加された`skk`をダブルクリック
    - Punctuation Style: Latin
    - Initial Input Mode: Direct Input
    - Page Size: 7
    - Return-key does not insert new line on commit: off
    - Candidate: Vertical
    - Number candidate of ...: 2
    - Show Annotation: on
    - Keys to Select...: Qwerty Center Row (a,s,d,...)
    - Dictionary and Rules
        - Rule: AZIK_en
- `System Tray`上の`fcitx`を右クリック-> `Restart`
        
ルールのAZIK_enはAZIKを改変したものです．
