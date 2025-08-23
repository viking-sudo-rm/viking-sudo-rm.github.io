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

<p>Will is an incoming Assistant Professor at the Toyota Technical Institute at Chicago and currently a Young Investigator at the Allen Institute for AI. He received his PhD from New York University working with Tal Linzen and Ashish Sabharwal, supported by an NSF graduate research fellowship and Two Sigma PhD fellowship. A major focus of Will’s research has been developing theory on the computational power and limitations of transformers, with an eye towards guiding the analysis and design of new architectures and inference methods. More generally, he is interested in theoretical computer science, computational linguistics, and the science of deep learning.</p>

<!-- <p>I am a Ph.D. student at the <a href="https://cds.nyu.edu/">CDS</a> at <a href="https://www.nyu.edu/">NYU</a>, where I am advised by <a href="https://tallinzen.net/">Tal Linzen</a>. I also work closely with <a href="https://allenai.org/team/ashishs">Ashish Sabharwal</a> at <a href="https://allenai.org/">AI2</a>, where I used to be a <a href="https://allenai.org/predoctoral-young-investigators">PYI</a>. My Ph.D. is supported by an <a href="https://www.nsfgrfp.org/resources/about-grfp/">NSF graduate research fellowship</a>, <a href="https://www.twosigma.com/community/academic-partnerships/team-phd-fellowship/">Two Sigma Ph.D. Fellowship</a>, and by <a href="https://allenai.org/">AI2</a>.</p>

<p>My research uses formal methods to better understand the capabilities and limitations of <b>language models</b>. I've worked on characterizing the <b>computational power of transformers</b> for representing linguistic structure and solving reasoning problems. I've also worked on understanding the aspects of <b>semantics that can be learned from co-occurrence patterns</b> in a large text corpus. Overall, I am interested in building out theoretical foundations for the alchemy of large language models. Why have LMs been successful? What are their limitations? How can we more systematically build and deploy them?</p> -->

<p><b>Contact:</b> <code>willm[æt]{nyu,allenai,ttic}.edu</code> or <a href="https://www.admonymous.co/lambdaviking">here</a> for anonymous feedback.</p>

<p><b>Potential PhD students:</b> I will be recruiting PhD students to start in 2026. If you would like to work with me, please apply to TTIC and mention my name in your application!</p>

<!-- <p>Outside of research, I like exploring New York City by foot, train, and boat. I like cooking new things and trying hole-in-the-wall restaurants. I also play basketball, ping pong, and Age of Empires II.</p> -->

<br /> <br />

<h2><a href="{{ '/blog/' | relative_url }}" style="color: inherit;">Latest posts</a></h2>
<div>{%- include latest_posts.html %}</div>

## Publications

<div class="publications">

{% bibliography -f {{ site.scholar.bibliography }} %}