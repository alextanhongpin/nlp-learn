import nltk

from nltk.tokenize import RegexpTokenizer, regexp_tokenize, BlanklineTokenizer, WhitespaceTokenizer, LineTokenizer, SpaceTokenizer
from nltk.tokenize.util import spans_to_relative, string_span_tokenize


text = "Don't hesitate to ask questions"
text2 = "This is a breaking news.\n A godzilla has been discovered in Tokyo city."
tokenizer = RegexpTokenizer('[\w]+')

print tokenizer.tokenize(text)

print regexp_tokenize(text, pattern='\w+|\$[\d\.]+\S+')

# Tokenize whitespace
tokenizer = RegexpTokenizer('\s+', gaps=True)
print tokenizer.tokenize(text)

# Select only words starting with capital letters
capt = RegexpTokenizer('[A-Z]\w+')
print capt.tokenize(text2)

print BlanklineTokenizer().tokenize(text2)

print WhitespaceTokenizer().tokenize(text2)

print LineTokenizer(blanklines='keep').tokenize(text2)
print LineTokenizer(blanklines='discard').tokenize(text2)

# SpaceTokenizer works similar to .split('')
print SpaceTokenizer().tokenize(text2)

# Returns the sequence of tuples that are offsets of the tokens
# in a sentence:
print list(WhitespaceTokenizer().span_tokenize(text2))

# Returns the sequence of relative spans
print list(spans_to_relative(WhitespaceTokenizer().span_tokenize(text2)))

# Returns the offsets of tokens in text2 by splitting at each incidence of the separator:
print list(string_span_tokenize(text2, ""))