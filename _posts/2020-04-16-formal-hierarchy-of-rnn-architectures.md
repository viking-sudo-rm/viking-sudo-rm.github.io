---
layout: distill
title: "A Formal Hierarchy of RNN Architectures"
description: "Summary of the ACL 2020 paper"
tags:
date: 2020-04-16
featured: false
usemathjax: true

authors:
  - name: William Merrill
    url: "/"
    affiliations:
      name: AI2

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

This post is about [*A Formal Hierarchy of RNN Architectures*](https://arxiv.org/abs/2004.08500), which was joint work between myself, Gail Weiss, Yoav Goldberg, Roy Schwartz, Noah Smith, and Eran Yahav. Compared to the original paper, this post is more of a summary, and will attempt to explain the significance of the results assuming less familiarity with formal language theory.

## Background

Understanding the practical capacity of neural network architectures is an important question for both the design of new architectures and the interpretability of current ones. By "practical capacity", we mean the classes of tasks that an architecture can discover solutions to via standard training methods. Since we are mostly interested in NLP here, another way to describe this is the types of grammars that a trained neural network can learn to implement. It has been known since [Siegelmann and Sontag (1992)](https://dl.acm.org/doi/10.1145/130385.130432) that RNNs with infinite time and precision are Turing-complete; however, these unrealistic assumptions make this a bad formal model for practical learnable capacity.

Over the last year or two, several works have addressed this by relating deep NLP architectures like RNNs to existing formal models in automata theory. [Weiss et al. (2018)](https://arxiv.org/abs/1805.04908) showed a connection between LSTMs and counter machines (CMs), and demonstrated how LSTMs learn to count to solve certain formal tasks that other RNNs cannot solve. Building on this, [Merrill (2019)](https://arxiv.org/abs/1906.01615) formalized the notion of a saturated network (a finite-precision approximation of a continuous RNN) and related the capacity of different saturated RNNs to different classes of formal languages. [Peng et al. (2018)](https://arxiv.org/abs/1808.09357) explored RNN capacity along a different axis: whether or not their internal computation can be simulated by a weighted finite state machine (WFA).

## The Hierarchy

The goal of this paper is to unify these independent threads of research by further exploring the connection between formal models like saturated RNNs, CMs, and WFAs. We place all of these models into a two dimensional hierarchy defined by two formal properties: rational recurrence and space complexity. As defined by [Peng et al. (2019)](https://arxiv.org/abs/1808.09357), an RNN is *rationally recurrent* if its recurrent state can be computed by a WFA. *Space complexity*, related to the concept in analysis of algorithms, measures how much memory is available to a model.

We present new results characterizing models in terms of these properties. For example, we prove the saturated LSTM is not rationally recurrent, which was previously an open question. We also show that general CMs are not rationally recurrent. However, we explore restricted classes of counter machines that are. While the main focus of the paper is on RNNs, we also present results analyzing memory networks and transformers in the same terms. Together, these results provide a hierarchy of RNNS and related models in terms of the functions that their hidden states can express.

## Language Expressiveness

Once we have derived these characterizations, we use them to demonstrate formal languages that separate the capacities of different RNNs. We add a 1 or 2-layer feedforward "pooler" after the final RNN state and view this full model as a language acceptor. Here are some of the results in this vein, stated more formally. Let $D_k$ denote the capacity of an RNN with a $k$-layer pooler, and let s-$X$ denote the saturated version of architecture $X$.

$$ a^nb^n \in D_1(\textrm{s-LSTM}) $$
$$ a^nb^n \not\in D_1(\textrm{s-QRNN}) $$

The QRNN with a 1-layer pooler cannot recognize $a^nb^n$, whereas the LSTM can.

$$ a^nb^n \in D_1(\textrm{WFA}) $$

While the rationally recurrent s-QRNN cannot recognize $a^nb^n$, a WFA actually can! We provide an existence proof using some linear algebra, and then provide a method through which the proof can be extended to construct an example WFA.

$$ a^nb^n \in D_2(\textrm{s-QRNN}) $$

Adding a second linear layer (or using two s-QRNN layers) allows us to recognize $a^nb^n$ with an s-QRNN. Does this mean the hierarchy dissolves as the pooler is strengthened?

$$ a^nb^n\Sigma^* \in D_1(\textrm{s-LSTM}) $$
$$ a^nb^n\Sigma^* \not\in D(\textrm{s-QRNN}) \; \textrm{for any $D$} $$

No, the hierarchy persists, even for stronger decoders. We provide a simple extension of $a^nb^n$ that can be recognized by an s-LSTM with a 1-layer pooler, but can never be recognized by an s-QRNN, no matter how many layers the pooler has. We dub the technique used to prove this the *suffix attack*. It exploits the fact that the QRNN (compared to the LSTM) is fundamentally unable to detect when its state has reached an accepting configuration--thus, it cannot "stop" updating when the strings are padded with an arbitrary suffix. Since this is a general property, it can be directly adapted to other formal languages.

## Experiments

Finally, we run experiments testing whether unsaturated networks trained by gradient descent can learn variants of $a^nb^n$ and $a^nb^n\Sigma^*$. In every case, we find that the capacity of the saturated networks correctly predicts the outcome of the experiments. Thus, while our theoretical results largely focus on saturated networks, it seems that they also describe the practical behavior learned by unsaturated ones.
