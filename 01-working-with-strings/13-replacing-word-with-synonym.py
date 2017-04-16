import re
import nltk

class WordReplacer(object):
    def __init__(self, word_map):
        self.word_map = word_map
    def replace(self, word):
        return self.word_map.get(word, word)


replacer = WordReplacer({ 'congrats': 'congratulations' })

print replacer.replace('congrats')

