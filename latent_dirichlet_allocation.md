# Latent Dirichlet Allocation


How to find the best number of topics?

- optimize [coherence score](https://towardsdatascience.com/evaluate-topic-model-in-python-latent-dirichlet-allocation-lda-7d57484bb5d0)

## What is coherence score?

Coherence score is used in topic modelling to measure how interpretable the topics are to human.

In this case, topics are represented as the top N words with the highest probability of belonging to that particular topic.

In short, coherence score measures how similar those words are to each other.

Don't use the CV coherence score, which is the default for gensim, because it's not recommended by the [author](https://github.com/dice-group/Palmetto/issues/13#issuecomment-371553052).

Use UMass Coherence score instead.

Reference
- https://www.baeldung.com/cs/topic-modeling-coherence-score
- https://datascienceplus.com/evaluation-of-topic-modeling-topic-coherence/
