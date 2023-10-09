---
layout: distill
title: Theory of Saturated Neural Networks
description: Summarizing <i>Sequential Neural Networks as Automata</i>.
tags:
date: 2019-09-06
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

The main idea of my paper [Sequential Neural Networks as Automata](https://arxiv.org/abs/1906.01615) is that, if we making some simplifying assumptions about how neural networks work, we can derive a theory of network expressiveness (what formal languages can different architectures model?) that seems to agree with the classes of formal languages that different networks can learn when trained by gradient descent. Thus, this restricted theoretical capacity seems to be (potentially) a good proxy for the empirical learnable capacity of various networks.

## Saturated Networks

In the paper, I referred to the simplified network whose capacity we can analyze as an *asymptotic* network. However, after talking with Gail Weiss, I now believe the term *saturated* is more descriptive, and plan to use this term going forward.

A neural network is a function $f(x, \theta)$ that is almost-everywhere differentiable with respect to the parameters $\theta$. Given such a function, we derive the saturated network $f'$ as

$$ f'(x, \theta) = \lim_{N \rightarrow \infty} f(x, N\theta) . $$

We define $ f'(x, \theta) $ over the domain of $(x, \theta)$ for which the limit above exists.

In a neural network, the effect of this transformation is to discretize all of the activations. For example, consider a neuron:

$$ \sigma(wx + b) $$

where $\sigma$ is the sigmoid function. When we take the limit of $\sigma(Nwx + Nb)$, the output of the neuron approaches either $0$ or $1$. This is what I mean by *discretization*.

After applying this discretization to the full network, we can analyze the computational capacity of the resulting discrete automaton. We also define a notion of space complexity associated with these saturated networks in the paper. Intuitively, this measure of complexity is just the number of configurations that the saturated network can have after reading a sequence of length $n$. For more details on this, consult [the paper](https://arxiv.org/abs/1906.01615).

## Summary of Results

By $L(M)$, we denote the set of formal languages that a machine $M$ can accept. Some key capacity results from the paper are as follows:

* $L(\textrm{ConvNet})$ is a proper subset of the regular languages
* $L(\textrm{RNN})$ is exactly the regular languages
* $L(\textrm{GRU})$ is exactly the regular languages
* $L(\textrm{LSTM})$ is a superset of the regular languages, and a subset of the real-time counter languages

The core results about the configuration complexity, some of which are analogous, are:

* ConvNet has $O(1)$ configurations
* RNN has $O(1)$ configurations
* GRU has $O(1)$ configurations
* LSTM has $O(n^k)$ configurations for hidden size $k$
* Attention has $2^{O(n)}$ configurations
* [StackNN](https://github.com/viking-sudo-rm/stacknn-core) has $2^{O(n)}$ configurations

There are some other results about attention/transformers that I'm not going to get into here, since they're not so neat. If you're interested though, I refer you to Section 4 of [the paper](https://arxiv.org/abs/1906.01615).

## Empirical Evidence

### Positive Evidence

The development of this theory was motivated by past empirical results about what RNNs are able to learn. Two types of tasks (counting and reversing) serve as relevant diagnostics for assessing the computational power of different architectures.

[Weiss et al.](https://arxiv.org/abs/1805.04908) show that LSTMs can learn to count, whereas RNNs and GRUs do not. Similarly, [Sugzgun et al.](https://arxiv.org/abs/1906.03648) observe that LSTMs can learn the 1-Dyck counter language, whereas other RNNs do not. This is predicted by the theory since saturated LSTMs can do counting, but saturated RNNs and GRUs are finite state.

[Hao et al.](https://arxiv.org/abs/1809.02836) show how stack neural networks can solve the (beyond counter language) task of reversing a string, whereas LSTMs fail badly on this. In my paper, I also showed that attention can solve this task. Both of the results are predicted by the theory, since stack neural networks and attention allow for exponential configurations, which are needed to reverse a string, whereas LSTMs are limited to polynomial configurations.

### Negative Evidence

While I found that regularized neural networks display the counting pattern reported by [Weiss et al.](https://arxiv.org/abs/1805.04908), I also found that the unregularized LSTM, GRU, and RNN can all learn to model the language $a^nb^nc$, which requires counting. Thus, it might be more precise to say that the saturated theory seems to describe the learnable capacity of *regularized* networks. One possible interpretation of this is that the constraints imposed by regularization prevent the network from learning strategies beyond the saturated capacity.

## Proof Sketches

### RNN Capacity and Complexity

To show that $L(\textrm{RNN})$ is the regular languages, we show two directions of containment. 

First, we prove that the the regular languages are an upper bound. We do this by showing that the configuration complexity of the RNN is finite, i.e. $O(1)$. Since each neuron has two possible values ($-1$ and $1$), and there are $k$ neurons in the state, the number of configurations of the state vector is $O(2^k) = O(1)$.

The other direction is a little more complicated. We need to construct an RNN to simulate an arbitrary finite state machine. A construction for this is provided in Lemma B.1.

### LSTM Capacity and Complexity

In the LSTM case, even when we discretize the network, we get a model with more than finite state. This is because the LSTM's gating architecture is capable of counting ([Weiss et al.](https://arxiv.org/abs/1805.04908), 2018).

To show that the counter languages are an upper bound, we write the saturated gate network for a particular counter state neuron $c$ as follows:

<!-- For some reason, the normal \lim_ is not working here. Neither does f_tc_{t-1}. I guess -->

$$ \underset{N \rightarrow \infty}{\lim} c_t $$

$$ = \underset{N \rightarrow \infty}{\lim} fc_{t-1} + i{\tilde c}_t $$

$$ = \underset{N \rightarrow \infty}{\lim} ac_{t-1} + b $$

where $a$ is $0$ or $1$ and $b$ is $-1$, $0$, or $1$. This equation parameterizes a real-time counter machine update. Thus, the counter languages are an upper bound on the saturated LSTM capacity.
