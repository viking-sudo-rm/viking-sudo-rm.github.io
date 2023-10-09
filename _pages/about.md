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

<p>My research leverages linguistic and computational theory to better understand deep learning. I've worked on characterizing the <b>computational power of transformers</b> for representing linguistic structure and solving reasoning problems. I've also analyzed the types of semantics that can be learned distributionally, i.e., the <i>language decipherment problem</i> faced by today's large language models.</p>

<p><b>New:</b> Give me <a href="https://www.admonymous.co/lambdaviking">anonymous feedback</a>!</p>

<p>Outside of research, I like exploring New York City by foot and boat, playing basketball and Age of Empires II, and nerding out about dead languages.</p>

<br /> <br />

<h2><a href="{{ '/blog/' | relative_url }}" style="color: inherit;">Latest posts</a></h2>
<div>{%- include latest_posts.html %}</div>

## Publications

<div class="publications">

{% bibliography -f {{ site.scholar.bibliography }} %}