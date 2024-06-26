---
layout: about
title: About
permalink: /
subtitle:

profile:
  align: left
  image: whiteboard-headshot.jpeg
  image_circular: true # crops the image to make it circular
  address: >

news: false  # includes a list of news items
latest_posts: false  # includes a list of the newest posts
selected_papers: false # includes a list of papers marked as "selected={true}"
social: false  # includes social icons at the bottom of the page
---

<p>I am a Ph.D. student at the <a href="https://cds.nyu.edu/">CDS</a> at <a href="https://www.nyu.edu/">NYU</a>, where I am advised by <a href="https://tallinzen.net/">Tal Linzen</a>. I also work closely with <a href="https://allenai.org/team/ashishs">Ashish Sabharwal</a> at <a href="https://allenai.org/">AI2</a>, where I used to be a <a href="https://allenai.org/predoctoral-young-investigators">PYI</a>. My Ph.D. is supported by an <a href="https://www.nsfgrfp.org/resources/about-grfp/">NSF graduate research fellowship</a>, <a href="https://www.twosigma.com/community/academic-partnerships/team-phd-fellowship/">Two Sigma Ph.D. Fellowship</a>, and by <a href="https://allenai.org/">AI2</a>.</p>

<p>My research uses formal methods to better understand the capabilities and limitations of <b>language models</b>. I've worked on characterizing the <b>computational power of transformers</b> for representing linguistic structure and solving reasoning problems. I've also worked on understanding the aspects of <b>semantics that can be learned from co-occurrence patterns</b> in a large text corpus. Overall, I am interesting in building out theoretical foundations for the alchemy of large language models. Why have LMs been successful? What are their limitations? How can we more systematically understand design choices around pretraining and deployment?</p>

<p>
<b>Contact:</b> <code>willm[æt]nyu.edu</code> or <a href="https://www.admonymous.co/lambdaviking">here</a> for anonymous feedback
</p>

<p>Outside of research, I like exploring New York City by foot, train, and boat. I like cooking new things and trying hole-in-the-wall restaurants. I also play basketball, ping pong, and Age of Empires II.</p>

<br /> <br />

<h2><a href="{{ '/blog/' | relative_url }}" style="color: inherit;">Latest posts</a></h2>
<div>{%- include latest_posts.html %}</div>

## Publications

<div class="publications">

{% bibliography -f {{ site.scholar.bibliography }} %}