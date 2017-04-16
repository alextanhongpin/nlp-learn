import nltk

from nltk.tokenize import TreebankWordTokenizer, WordPunctTokenizer

text = "Have a nice day. I hope you find the book interesting. Don't hesitate to ask questions."

# TreebankWordTokenizer works by separating contractions
tokenizer = TreebankWordTokenizer()
print tokenizer.tokenize(text)


# WordPunctTokenizer provides splitting by making punctuations an entirely new token
tokenizer = WordPunctTokenizer()
print tokenizer.tokenize(text)