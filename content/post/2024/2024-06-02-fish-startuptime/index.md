---
title: fishの起動時間
author: atusy
date: '2024-06-02'
slug: fish-startuptime
categories: [fish]
tags: []
output:
  'blogdown::html_page':
    md_extensions: +east_asian_line_breaks+task_lists
highlightjs:
  - fish
---


fishの起動時間は`fish -i -c "fish_prompt; exit 0"`の実行時間で測るとよさそうです。

-   `-i`オプションにより設定ファイルの実行時間を含む
-   `-c`オプションに`fish_prompt`を呼ぶことでプロンプトの決定にかかる時間を含む

コマンドのベンチマークに便利な[hyperfine](https://github.com/sharkdp/hyperfine)を使うとこんな感じ。
平均45.8msとのことで、十分に高速かと思います。

    > hyperfine -w 5 -r 50 -N 'fish -i -c "fish_prompt; exit 0"'
    Benchmark 1: fish -i -c "fish_prompt; exit 0"
      Time (mean ± σ):      45.8 ms ±   2.7 ms    [User: 32.9 ms, System: 16.5 ms]
      Range (min … max):    41.6 ms …  55.2 ms    50 runs

`fish_prompt`の呼び出しが必要そうと気付いたきっかけは、呼び出しなしでのベンチマーク結果（22.8ms）と、体感の起動速度に差があったためでした。
当時は`fish_prompt`の最適化前だったのもあり、気付きやすかった模様。
私はプロンプトにKubernetesで利用中のContextやNamespaceを表示するようにしていますが、`kubectl`コマンドがどうにも遅いようですね。
`kubectl`の代わりに`gojq`で設定ファイルを読むようにして、最適化し、正味の起動時間を100msほど改善しました。

以下は`fish_prompt`を含まない起動時間。

    > hyperfine -w 5 -r 50 -N 'fish -i -c "exit 0"'
    Benchmark 1: fish -i -c "exit 0"
      Time (mean ± σ):      22.8 ms ±   1.2 ms    [User: 15.5 ms, System: 8.9 ms]
      Range (min … max):    20.9 ms …  25.6 ms    50 runs

ちなみに`fish`の関数をベンチマークしたい場合は`time`関数が便利です。
以下は`fish_prompt`を10回実行するのにかかる時間を計測する例。

    > time for i in ( seq 10); fish_prompt >/dev/null; end

    ________________________________________________________
    Executed in  140.37 millis    fish           external
       usr time   95.23 millis   32.20 millis   63.03 millis
       sys time   49.39 millis   17.81 millis   31.58 millis

**ENJOY!**
