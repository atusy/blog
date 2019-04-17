---
title: Form
author: ~
date: '2019-04-17'
slug: netlify-forms
categories: []
tags: []
---

<form name="contact" method="POST" data-netlify="true" data-netlify-recaptcha="true" netlify-honeypot="bot-field">
  <p>
    <label><input type="text" name="name" placeholder="Name"/></label>   
  </p>
  <p>
    <label><input type="email" name="email" placeholder="Email Address" /></label>
  </p>
  <p>
    <label><textarea name="message" cols = "40" rows = "10" placeholder="Message"></textarea></label>
  </p>
  <p>
    <button type="submit">Send</button>
  </p>
  <p>
    <label style="visibility:hidden"><input name="bot-field" /></label>
  </p>
</form>
