import nltk
from nltk.corpus import stopwords

print stopwords.fileids()
stops = set(stopwords.words('english'))

print stops

words = "Don't hesitate to ask questions".split(" ")

print [word for word in words if word not in stops] 


def para_fraction(text):
    s = set(stopwords.words('english'))
    para = [w for w in text if w.lower() not in s]
    return len(para) / len(text)


print nltk.corpus.reuters.words()
print para_fraction(nltk.corpus.reuters.words())
print para_fraction(nltk.corpus.inaugural.words())