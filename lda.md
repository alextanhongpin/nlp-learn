# Gibbs sampling

## What

Gibbs sampling is a Markov Chain Monte Carlo (MCMC) algorithm for obtaining a sequence of observations which are approximated from a specified multivariate probability distribution, when direct sampling is too difficult.

- http://users.umiacs.umd.edu/~resnik/pubs/LAMP-TR-153.pdf
- https://kieranrcampbell.github.io/blog/2016/05/15/gibbs-sampling-bayesian-linear-regression.html
- https://towardsdatascience.com/from-scratch-bayesian-inference-markov-chain-monte-carlo-and-metropolis-hastings-in-python-ef21a29e25a


## Review datasets

https://kavita-ganesan.com/user-review-datasets/#.XVYd7pMzbBI

## Building the LDA topic modelling with gensim

What input do we need? a list of sentences.

1. split sentence into individual tokens
2. perform cleansing by lowercasing them, removing stopwords, lemmatizing/stemming them

```python
tokenizer = RegexpTokenizer(r’\w+’)
def tokenize(docs):
	result = []
	for doc in docs:
		doc = doc.lower()
		tokens = tokenizer.tokenize(doc)
		tokens = [token for token in tokens if token not in STOPWORDS]
		tokens = [stem(token) for token in tokens]
	return result

texts = tokenize(docs)
id2word = gensim.corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=id2word, num_topics=5)
```
- how do we use the lda model?
- how to determine the best number of topics?
- how do we evaluate the model performance? 
- how do we use this to show recommendations

