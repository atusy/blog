---
title: サイドバーにシェアボタンを追加
author: ~
date: '2019-02-08'
slug: sns-buttons
categories: [Hugo]
tags: [SNS]
---

やっぱり Share ボタンは欲しいよねということで雑に実装．

## アイコンの用意

### fontawesome の利用を宣言

`partials/head-custom.html` に以下を追記

```{html}
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.1/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
```

### はてブ用に fa-hatena を作る

`static/style.css` に以下を追記．

```{css}
/* Font Awesome hatena bookmark */
.fa-hatena:before {
    content: "B!";
    font-family: Verdana;
    font-weight: bold
}
```

参考: https://hayashikejinan.com/webwork/css/913/


## サイドバーを記述

1. `themes/hugo-bootstrap/layouts/partials/sidebar.html` を `partials/sidebar.html` にコピー
1. Web で拾ってきたコードの一部を改変して追記

    ```{html}
    <h4>Share</h4>
    
    <!-- use font awsome -->
    <section class="section sns_parent">
      <div class="container sns_section">
          <span class="sns_button twitter">
            <a href="http://twitter.com/intent/tweet?url={{ .Permalink }}&text={{ .Title }}" target="_blank" title="Tweet"><i class="fab fa-twitter"></i></a>
          </span>
          <span class="sns_button hatena">
            <a href="http://b.hatena.ne.jp/add?mode=confirm&url={{ .Permalink }}&title={{ .Title }}" target="_blank" title="hatena"><i class="fa fa-hatena"></i></i></a>
          </span>
          <span class="sns_button facebook">
            <a href="http://www.facebook.com/sharer.php?u={{ .Permalink }}&t={{ .Title }}" target="_blank" title="Facebook"><i class="fab fa-facebook"></i></a>
          </span>
          <span class="sns_button google">
            <a href="https://plus.google.com/share?url={{ .Permalink }}" target="_blank" title="google+"><i class="fab fa-google-plus"></i></a>
          </span>
          <span class="sns_button pocket">
            <a href="http://getpocket.com/edit?url={{ .Permalink }}&title={{ .Title }}" target="_blank" title="pocket"><i class="fab fa-get-pocket"></i></a>
          </span>
      </div>
    </section>
    ```

css ちゃんとしてないのでムダな `span` やら `div` がいっぱい．

参考: https://aakira.app/blog/2018/08/share/

