---
layout: distill
title: "The State of Interpretability in NLP"
description: "Thoughts from my experience at ACL 2019"
tags:
date: 2019-08-06
featured: false
usemathjax: true

authors:
  - name: William Merrill
    url: "/"
    affiliations:
      name: Yale

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

This post is a summary of my thoughts and experiences at ACL 2019, focused around the theme of interpretability. After spending most of the summer thinking about things besides neural networks, I was abruptly thrown back into things upon arriving in Florence. I spent a lot of my downtime with friends from Yale that I was staying with. On the other hand, I also met my future colleagues at AI2 and many other young researchers who are interested in similar issues of the interpretability and formal analysis of neural networks. In this way, the conference felt like a soft threshold between old and new.

There were plenty of exciting things going on at the main conference, from work on incorporated graph representations into transformers to the development of more energy-efficient non-autoregressive NLP models. In this post, though, I'm going to focus on parts that I was most directly involved in, which were the Blackbox NLP workshop on interpretability and the Deep Learning and Formal Languages (DELFOL) workshop.

# Blackbox NLP

This was the second iteration of the Blackbox workshop. While the last Blackbox at EMNLP was also quite large and interesting, it had felt to me like a quite interdisciplinary meeting of researchers doing very different things. In contrast, I got the impression at this year's meeting that a community of interpretability-minded researchers with similar goals and methods has formed. This is consistent with the wider interest that interpretability has sparked in the larger NLP community and the number of interpretability papers presented in the main conference. In the closing panel of the workshop, it was mentioned that perhaps interpretability would become a session within the conference at the next ACL meeting instead of a supplementary workshop.

One of the main goals of interpretability research is to assess what kinds of information is encoded in different representations within a neural network. In particular, people (including myself) are interested in how different models encode grammatical information. Several methods were discussed for addressing this question, including attention, probing, representational similarity analysis (RSA).

## Attention

A classical way of interpreting whether networks encode grammatical information is by looking at attention alignments. For example, we might expect that, if there is a dependency between words $i$ and $j$, then position $i$ in the network should attend to position $j$. While this probably works to some degree, attention maps can often get messy. Also, as [Serrano et al.](https://arxiv.org/abs/1906.03731) pointed out in their work at the main conference, perturbing the attention distribution has surprisingly little effect on a network's behavior. Thus, we might want to look to other methods for interpreting neural representations.

## Probing

Probing refers to using a linear classifier to try to recover some kind of information, say part of speech information, from some representation within a model. This has been a standard way of interpreting neural representations throughout the last year. The underlying assumption is that, if information is recoverable in a single linear layer, then it is probably strongly encoded in the representation. As was pointed out to me by [Jungo Kasai](https://homes.cs.washington.edu/~jkasai/), one pitfall of this method is that it just assesses whether or not the information of interest is encoded in a representation, not to what degree it is there. For example, if a small amount of the representation in some network is representing grammatical information, whereas the rest of it is representing spurious correlations between words, probing would still suggest that that layer is encoding grammar. In such a case, is it really reasonable to conclude that a grammatical representation is an important part of the behavior which the network is learning?

## RSA

An alternate approach to the same problem is RSA, which is not to be confused with the cryptographic protocol of the same name. RSA sidesteps the issue with probing by measuring the degree to which two representations are correlated, not whether the information from one can be recovered from the other.

Formally, RSA is a method of computing the similarity between two representations $X$ and $Y$. We assume that we do not have the direct ability to compare $x$ to $y$, but instead have two internally defined similarity measures $d_X(x_1, x_2)$ and $d_Y(y_1, y_2)$. These measures need not be symmetric.

To get an overall measure of similarity, we compute a similar matrices $M(X)$ and $M(Y)$ where

$$ M(X)_{ij} = d_X(x_i, x_j) $$

and analogously for $Y$. Once we have these matrices, we compute an overall measure of similarity by taking the correlation between them. I find RSA to be a quite exciting method for future research, as it avoids some of the pitfalls of probing while also being very easy (perhaps easier than probing) to implement. This is not to say that probing should be abandoned completely, as being able to verify the same results with different methods increases their confidence. I recall hearing a talk at ACL in which RSA was already applied to transformer representations and replicated probing findings, although I unfortunately cannot find the paper which reported this.

## Conclusion

Probing and RSA are two good methods for understanding what information is encoded in some representation within a trained network. This is still a slightly different question than asking what information is particular relevant for the decision that a network makes given some input, which can be addressed using gradient methods or perturbation studies. I think that interpreting representations and interpreting decisions are both interesting questions.

Additionally, both of these questions have analogs in the formal domain, where we can analyze what representations different neural network hidden states can encode, or what classes of formal languages a certain architecture can accept. As others at ACL also mentioned, I would like to see future work connecting empirical interpretability research to the formal analysis that has been done.

Finally, as many people expressed during the conference, I think that a good goal for the next year is progress towards constructive interpretability work. In other words, our interpretation of networks should allow us to make smarter architectures.

# DELFOL

DELFOL was the venue for formal work at ACL 2019. Given its somewhat esoteric topic, this workshop was quite small, but I found it really exciting. To me, the following three questions captured a lot of the work that people were presenting:

1. Assess the learnable capacity of neural network models using empirical studies
2. Identify formal properties of neural architectures that lead to different kinds of inductive bias or learnable/representational capacity
3. "Distill" neural network models into smaller, more interpretable discrete models

## Empirical Experiments about Learnability

On the empirical front, [Suzgun et al.](https://arxiv.org/abs/1906.03648) reported that LSTMs generalizably learn to model the 1-Dyck language, which consists of parenthetic expressions with one type of parentheses. Other types of RNNs, on the other hand, were not able to do this. Additionally, LSTMs could not model 2-Dyck, but could model independently mixed versions of 1-Dyck.

Since 1-Dyck is a counter language, this is further evidence that LSTMs can count, unlike other kinds of RNNs. Additionally, since 2-Dyck is a context-free language that requires more memory than is available to counter machines, we have further experimental evidence that LSTM memory, like counter machine memory, is not sufficient for complex hierarchical representations. As [Bob Frank](https://bobfrank1.github.io/) summarized in his invited talk at DELFOL, LSTMs also struggle to do other memory intensive context-free things, like reversing strings.

While [my paper](https://arxiv.org/abs/1906.01615) at DELFOL was mostly theoretical results, I also had some experimental stuff that agreed with these conclusions.

## Formal Analysis of Inductive Bias and Capacity

### Saturated Networks

Building on work done by [Weiss et al.](https://arxiv.org/abs/1805.04908), [my paper](https://arxiv.org/abs/1906.01615) at DELFOL developed a theory of **saturated networks**, or networks where the activation functions are restricted to their asymptotic values instead of intermediate rational values. I proved that saturated RNNs and GRUs are equivalent to finite-state automata in capacity, whereas saturated LSTMs are equivalent to a restricted class of counter machines. [Bob Frank](https://bobfrank1.github.io/) also synthesized my results and Weiss et al.'s results in his invited talk.

I think these theoretical results about saturated networks are interesting because they agree with empirical results (see previous section) about the types of languages that natural networks are empirically able to learn and generalize. This suggests that the capacity of the saturated network might represent something like the inductive bias or effective learnable capacity of the general network.

### Other Formal Properties

In his talk, [Bob Frank](https://bobfrank1.github.io/) also mentioned other ways of understanding the abilities of different networks. In particular, he mentioned studying the closure properties of representable or learnable languages as a potential way to build a theory. Another notable formal property that he mentioned was semilinearity. In his talk, [Noah Smith](https://homes.cs.washington.edu/~nasmith/) mentioned rational recurrence as one way to analyze different neural architectures. While less linguistically motivated, this property is nice because of its connections to classical finite-state methods in NLP and the interpretability that comes along with this.

### Distillation

Finally, a general theme at DELFOL that I found especially interesting was distillation. This refers to converting a neural network to a smaller and more interpretable discrete model which approximates the same behavior. This has a variety of practical benefits: deployment on smaller devices, interpretability, and possibly regularization, to name a few. I think one of the reasons why I find this topic interesting is because it is a way for theory to provide very concrete solutions to practical problems.

As I see it, there are two main ways that distillation has been done. [Weiss et al.](https://arxiv.org/abs/1711.09576) pioneered the **query-based** approach, which involves using the [L* algorithm](https://people.eecs.berkeley.edu/~dawnsong/teaching/s10/papers/angluin87.pdf) to learn a finite-state machine using black-box queries to a neural network. The other type of distillation is **spectral**, which [Rémi Eyraud](https://pageperso.lis-lab.fr/~remi.eyraud/WP/) spoke about at DELFOL. This involves building a Hankel matrix for some language and then using SVD to extract a smaller matrix representing a weighted finite-state automaton. While these are the two methods that have been investigated, I'm interested in other ways to achieve distillation, and I have been doing some preliminary experiments using other methods. More on that to come!