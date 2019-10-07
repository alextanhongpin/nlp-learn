# nlp-with-python
Understanding the concepts of natural language processing with python.

## Stopwords

List of stopwords: https://gist.github.com/sebleier/554280

On dealing with stopwords: remove generic stopwords, but also don't forget to find the domain-specific stopwords. This is typically the name of the product itself, or verbs associated with the product, e.g. for computer games, the word `computer`, `game`, `playing` could be the stopwords, since it is describing the product itself.

# Text analytics 

- https://www.datacamp.com/community/tutorials/text-analytics-beginners-nltk
- https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html


## Text extraction

E.g. extracting keywords from resume. But there could be typo (e.g. workd, when what we want is work). Can levenshtein be used with regex? Apparently there is an approximate string matching regex in the regex module for python not the re module.

## NLP - Text Summarization
https://machinelearningmastery.com/gentle-introduction-text-summarization/

https://medium.com/m/global-identity?redirectUrl=https%3A%2F%2Ftowardsdatascience.com%2Fa-quick-introduction-to-text-summarization-in-machine-learning-3d27ccf18a9f

https://medium.com/m/global-identity?redirectUrl=https%3A%2F%2Ftowardsdatascience.com%2Funderstand-text-summarization-and-create-your-own-summarizer-in-python-b26a9f09fc70
https://medium.com/jatana/unsupervised-text-summarization-using-sentence-embeddings-adb15ce83db1
https://blog.floydhub.com/gentle-introduction-to-text-summarization-in-machine-learning/

https://www.geeksforgeeks.org/ml-text-summarization-of-links-based-on-user-query/
https://medium.com/m/global-identity?redirectUrl=https%3A%2F%2Fhackernoon.com%2Ftext-summarizer-using-deep-learning-made-easy-490880df6cd

https://www.analyticsvidhya.com/blog/2018/11/introduction-text-summarization-textrank-python/
https://machinelearningmastery.com/gentle-introduction-text-summarization/
https://catalog.ldc.upenn.edu/LDC2012T21

https://www.tensorflow.org/tutorials/keras/basic_classification

https://www.analyticsvidhya.com/blog/2018/04/a-comprehensive-guide-to-understand-and-implement-text-classification-in-python/

https://www.digitalvidya.com/blog/document-classification-python-machine-learning/
https://medium.com/mlrecipies/document-classification-using-machine-learning-f1dfb1171935
https://cloud.google.com/blog/products/gcp/problem-solving-with-ml-automatic-document-classification

https://www.kdnuggets.com/2015/01/text-analysis-101-document-classification.html
https://blog.christianposta.com/microservices/the-hardest-part-about-microservices-data/


also take a look at SQUAD standford question answering database
https://databricks.com/tensorflow/examples
https://github.com/aymericdamien/TensorFlow-Examples
https://adventuresinmachinelearning.com/python-tensorflow-tutorial/
https://www.geeksforgeeks.org/ml-text-summarization-of-links-based-on-user-query/

https://medium.com/m/global-identity?redirectUrl=https%3A%2F%2Ftowardsdatascience.com%2Fnlp-building-a-question-answering-model-ed0529a68c54
https://towardsdatascience.com/automatic-question-answering-ac7593432842?gi=dae76ddf5325
https://paperswithcode.com/task/question-answering
https://radimrehurek.com/gensim/tutorial.html
http://kavita-ganesan.com/gensim-word2vec-tutorial-starter-code/


https://www.searchtechnologies.com/blog/natural-language-processing-techniques
https://towardsdatascience.com/detecting-bad-customer-reviews-with-nlp-d8b36134dc7e
https://blog.insightdatascience.com/how-to-solve-90-of-nlp-problems-a-step-by-step-guide-fda605278e4e
https://medium.com/hackernoon/stepping-into-nlp-word2vec-with-gensim-e7c54d9a450a

https://towardsdatascience.com/hands-on-bayesian-statistics-with-python-pymc3-arviz-499db9a59501
https://www.python-course.eu/machine_learning_terminology.php

## Sequence-to-Sequence learning

https://towardsdatascience.com/nlp-sequence-to-sequence-networks-part-2-seq2seq-model-encoderdecoder-model-6c22e29fd7e1
https://blog.keras.io/a-ten-minute-introduction-to-sequence-to-sequence-learning-in-keras.html
https://towardsdatascience.com/understanding-encoder-decoder-sequence-to-sequence-model-679e04af4346

## Locality Sensitive Hashing (LSH)

- detect plagiarism in text
- recommendation

https://github.com/mattilyra/LSH/blob/master/examples/Introduction.ipynb
https://mattilyra.github.io/2017/05/23/document-deduplication-with-lsh.html
https://www.learndatasci.com/tutorials/building-recommendation-engine-locality-sensitive-hashing-lsh-python/
https://resteorts.github.io/record-linkage-tutorial/slides/03-lsh.pdf
https://towardsdatascience.com/understanding-locality-sensitive-hashing-49f6d1f6134
https://towardsdatascience.com/locality-sensitive-hashing-for-music-search-f2f1940ace23
https://medium.com/@himanshuit3036/locality-sensitive-hashing-finding-documents-similarity-6f12d4d83af
https://medium.com/engineering-brainly/locality-sensitive-hashing-explained-304eb39291e4
https://www.knoyd.com/blog/2017/7/30/facebook-group-scraper
https://thoughtbot.com/blog/recommending-blog-posts
https://pydata.org/london2018/schedule/presentation/30/
https://www.learndatasci.com/tutorials/building-recommendation-engine-locality-sensitive-hashing-lsh-python/
https://databricks.com/session/locality-sensitive-hashing-by-spark
https://www.mit.edu/~andoni/LSH/

https://medium.com/engineering-brainly/locality-sensitive-hashing-explained-304eb39291e4
https://en.m.wikipedia.org/wiki/Locality-sensitive_hashing
https://towardsdatascience.com/understanding-locality-sensitive-hashing-49f6d1f6134?gi=5b9309f16dce
https://en.m.wikipedia.org/wiki/Locality-sensitive_hashing
https://en.m.wikipedia.org/wiki/(1%2Bε)-approximate_nearest_neighbor_search
