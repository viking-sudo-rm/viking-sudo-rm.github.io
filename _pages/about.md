---
layout: about
title: About
permalink: /
subtitle:

profile:
  align: left
  image: headshot.jpg
  image_circular: true # crops the image to make it circular
  address: >

news: false  # includes a list of news items
latest_posts: false  # includes a list of the newest posts
selected_papers: false # includes a list of papers marked as "selected={true}"
social: false  # includes social icons at the bottom of the page
---

<p>I am a Ph.D. student at the <a href="https://cds.nyu.edu/">CDS</a> at <a href="https://www.nyu.edu/">NYU</a>, where I am advised by <a href="https://tallinzen.net/">Tal Linzen</a> and supported by an <a href="https://www.nsfgrfp.org/resources/about-grfp/">NSF graduate research fellowship</a> and by <a href="https://allenai.org/">AI2</a>.</p>

<p>My research develops theory to better understand what <b>language models</b> can do, as well as what they can't. I've worked on characterizing the <b>computational power of transformers</b> for representing linguistic structure and solving reasoning problems. I've also analyzed the aspects of <b>semantics that can be learned from co-occurrence patterns</b> as a way to understand the potential of self-supervised learning.</p>

<p><b>New:</b> Give me <a href="https://www.admonymous.co/lambdaviking">anonymous feedback</a>!</p>

<p>Outside of research, I like exploring New York City by foot, train, and boat. I like cooking new things and trying hole-in-the-wall restaurants. I also play basketball, ping pong, and Age of Empires II.</p>

<br /> <br />

<h2><a href="{{ '/blog/' | relative_url }}" style="color: inherit;">Latest posts</a></h2>
<div>{%- include latest_posts.html %}</div>

## Publications

<div class="publications">

{% bibliography -f {{ site.scholar.bibliography }} %}