---
layout: page
title: ""
---

![plot1](../public/mds.png)

<ul class="post">
  {% for post in site.posts %}
    <li>
      <span class="post-date post-date-home">{{ post.date | date: "%b %-d, %Y" }}</span>
      <h3>
        <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
      </h3>
    </li>
  {% endfor %}
</ul>
