---
layout: distill
title: "Voynich2Vec: Word2Vec Analysis of the Voynich Manuscript"
description: "Can NLP help us decipher the enigmatic manuscript?"
tags:
date: 2018-04-15
featured: false
# usemathjax: true

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

Last semester in school, I worked on a project where we attempted to build word embeddings from the Voynich manuscript and use them to learn something about the linguistic structure (or lack thereof) within the text. You can check out our [codebase](https://github.com/viking-sudo-rm/voynich2vec) or our [paper](assets/pdf/yale/voynich2vec.pdf). The reason why this methodology is exciting is that building word embeddings is completely unsupervised. This makes it a very appealing methodology for decipherment-like tasks. If done properly, we should be able to visualize the word embedding space and understand something about the relationship between words and characters in the manuscript!

However, several issues make this methodology more complicated for Voynich. First, there are problems with transcription and word and sentence segmentation. Several digitalized transcriptions of the manuscript exist, and they disagree in a surprising number of places. A second concern is the issue of data sparsity. Canonical methods for word embeddings are designed to be architecturally simple so that they can be applied to massive data sets (for example, all of Wikipedia). These models overcome their architectural shortcomings from being hit over the head with a lot of data: there is no inductive bias that tells them that *relocate* and *relocates* are systematically related, but if the model gets to see all of Wikipedia, it should be able to figure this out. On the other hand, in a low-resource setting like Voynich, the distribution of words is sparse enough that we probably will never see every form of each verb. We need a more complex model that has the ability to learn a generalizable notion of morphology. It seems feasible that there is enough signal in the data for a model to actually learn a meaningful model of Voynich morphosyntax even if the data is too sparse to build a meaningful representation of the syntactic space.

There's not much we can do to address the transcription concern except being principled about which transcription we adopt. However, there is recent work about building morphologically-informed word embeddings. In particular, our project utilized fastText embeddings, which were developed by Facebook research. FastText works by learning different embeddings for different subsequences of words and representing the embedding for the full word as a combination of these sub-embeddings. Intuitively, subsequences that are morphemes should contribute a meaningful vector to the full word vector, and subsequences that do not encode morphological information will have a representation close to zero. You can find the code to build these embeddings in the voynich2vec repository.

Our original project tried to analyze these vectors in three different ways:

1. **Morphosyntactic analysis.** We looked at how words with common suffixes were distributed in the Voynich embedding space. If a suffix contributes to where the word can appear (i.e., it carries morphosyntactic information), then we would expect words ending in it to cluster closely. Conversely, if it does not contribute to where the word can appear, this should mean that it is just a common suffix but not a morpheme. Excitingly, we found that some suffixes displayed said clustering, but others did not. Also interestingly, we found that some similar suffixes clustered together, which suggests that they are two different surface realizations of the same morpheme.
2. **Topic modelling.** We can build a bag-of-words representation of some section of the manuscript by summing the embeddings for the words on that page. This sum could possibly be weighted by a metric like TF-IDF. We did this and got some clustering by section, but nothing very conclusive.
3. **Unsupervised word alignment.** We attempted to use a method called MUSE to align two word embedding spaces. If this worked, this could give as an approximate mapping from Voynichese words to Latin words. Sadly, it did not work. Unsupervised alignment methods like MUSE rely on massive corpora. In our case, Voynich was so small that we only got noise. There has also been work done on semi-supervised word embeddings where two embedding spaces can be fully aligned from a small set of seed words (for example, just the month names).

Sadly, I haven't been able to work on this project much since the beginning of the summer, but I'm keeping track of a central list of ideas for future work [here](https://github.com/viking-sudo-rm/voynich2vec/issues). In particular, I think the most promising question is to extend our preliminary work on morphosyntactic analysis. As I describe in one of the [GitHub issues](https://github.com/viking-sudo-rm/voynich2vec/issues/9), methods have been developed in the NLP literature for inducing morphology from a vector space of word embeddings. This method could be used to generate a full morphological profile of Voynichese.