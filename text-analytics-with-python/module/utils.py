import html
from module.contractions import expand_contractions
from module.lemmatize import lemmatize_text
from module.tokenize import tokenize_text
from module.normalization import remove_special_characters, remove_stopwords


def normalize_corpus(corpus, lemmatize=True, tokenize=False):
    normalized_corpus = []
    for text in corpus:
        text = html.unescape(text)
        text = expand_contractions(text)
        if lemmatize:
            text = lemmatize_text(text)
        else:
            text = text.lower()
        text = remove_special_characters(text)
        text = remove_stopwords(text)
        if tokenize:
            text = tokenize_text(text)
            normalized_corpus.append(text)
        else:
            normalized_corpus.append(text)

    return normalized_corpus


from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


def build_feature_matrix(documents, feature_type='frequency'):
    feature_type = feature_type.lower().strip()

    if feature_type == 'binary':
        vectorizer = CountVectorizer(binary=True, min_df=1, ngram_range=(1, 1))
    elif feature_type == 'frequency':
        vectorizer = CountVectorizer(
            binary=False, min_df=1, ngram_range=(1, 1))
    elif feature_type == 'tfidf':
        vectorizer = TfidfVectorizer(min_df=1, ngram_range=(1, 1))
    else:
        raise Exception(
            'Wrong feature type entered. Possible values: "binary", "frequency", "tfidf"'
        )

    feature_matrix = vectorizer.fit_transform(documents).astype(float)
    return vectorizer, feature_matrix
