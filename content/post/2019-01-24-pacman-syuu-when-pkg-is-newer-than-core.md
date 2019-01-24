---
title: 'Warnning: newer than the core を放置せずに pacman -Syuu しとこう'
author: ~
date: '2019-01-24'
slug: pacman-syuu-when-pkg-is-newer-than-core
categories: [Archlinux]
tags: [pacman, manjaro]
---

`pacman -Syu`{.sh} でアップグレードした際に，`Warnning: newer than the core`といった警告が出ることがあります．

そんな時は `pacman -Syuu`{.sh} して新しすぎるパッケージをダウングレードしましょう．

放置するとパッケージの依存関係が壊れて，最悪の場合はブートしなくなります．

# ブートしなくなった場合の対策

1. ブートしなくなったディストロと同じディストロをUSBメモリなどから起動
1. ブートしなくなったディストロのインストールされたディスクをマウント
    - 例えば `/mnt` に
1. `pacman -Syuu --root /mnt/`{.sh}
1. リブート

参考: https://bbs.archlinux.org/viewtopic.php?pid=1827243#p1827243

## 対策方法発見までの過程

- ブートしなくなったのでとりあえず grub からのブートを試す
      - 参考: https://jp.linux.com/news/linuxcom-exclusive/418274-lco20140625

          ```{.grub}
          set pager=1
          ls # ディスク一覧かあ起動ディスクにあたりをつける
          ls (hd0,1)/ # 起動ディスクっぽいディスクの中身を確認
          cat (hd0,1)/etc/issue # ディストロを確認
          set root=(hd0,1)
          linux /boot/vmlinuz-3.13.0-29-generic root=/dev/sda1
          initrd /boot/initrd.img-3.13.0-29-generic
          boot
          ```
      -  `libidn2.so.0` がないと怒られる
- "libidn2.so.0 missing boot" でググる
      - [Manjaro stuck on boot screen: libidn2.so.4 missing](https://forum.manjaro.org/t/manjaro-stuck-on-boot-screen-libidn2-so-4-missing/72999)
          - 更に [こちら](https://forum.manjaro.org/t/stable-update-2019-01-23-kernels-mesa-browsers-nvidia-deepin-virtualbox/72986) に案内される
              - "newer than the core" と表示されるパッケージをダウングレードせよ
              - そういえばそんなパッケージが複数あったけど，起動しないのにどうやってダウングレードするのよ……．
        - [\[solved\]after upgrade  system doesn't boot anymore; libidn2.so.0 is missing](https://bbs.archlinux.org/viewtopic.php?pid=1827243#p1827243)
            - [先述の対策](#ブートしなくなった場合の対策)っぽい答えが載ってた．\
            > I created and booted an actual ArchLive USB. Then I mounted my disk to /mnt/ and did the following similar to https://wiki.archlinux.org/index.php/Pacman#Pacman_crashes_during_an_upgrade :
              
                ```{.sh}
                pacman -S pacman libpsl libidn2 --root /mnt/
                ```
- [ググった結果を合体させた](#ブートしなくなった場合の対策)
