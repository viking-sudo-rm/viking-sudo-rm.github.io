---
layout: distill
title: "Project: Improved Adversarial Robustness via Abstract Interpretation"
description: A course project for Foundations of Machine Learning at NYU
tags:
date: 2022-04-15
featured: false
usemathjax: true

authors:
  - name: William Merrill
    url: "/"
    affiliations:
      name: NYU

bibliography:

# Optionally, you can add a table of contents to your post.
# NOTES:
#   - make sure that TOC names match the actual section names
#     for hyperlinks within the post to work correctly.
#   - we may want to automate TOC generation in the future using
#     jekyll-toc plugin (https://github.com/toshimaru/jekyll-toc).
# toc:
#   - name: Introduction

---

This paper improves methods for certifying the adversarial robustness of neural networks using techniques from abstract interpretation. The idea is to pass regions of the input space (rather than specific inputs) through the network, and compute an upper bound on the loss over that region. We introduce some practical techniques to get a tighter upper bound on this loss compared to previous work.

You can find the final report [here](assets/pdf/foml-final-project.pdf). I had a lot of fun working on this project along with my coauthors Zachary DeStefano and Ildebrando Magnani!