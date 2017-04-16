import nltk

# text = nltk.word_tokenize("Pierre Vinken, 59 years old, will join as a nonexecutive director on ...")
# print(text)

r = input("Please write a text:\n")

print "The length of the text is: " + str(len(nltk.word_tokenize(r))) + " words"
print nltk.word_tokenize(r)