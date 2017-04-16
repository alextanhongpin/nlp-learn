"""
Tokenization may be defined as the process of splitting
the text into smaller parts called token.
"""

import nltk
from nltk.tokenize import sent_tokenize

text = "Welcome readers. I hope you find it interesting. Please do reply."

print sent_tokenize(text)

tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")

print tokenizer.tokenize(text)