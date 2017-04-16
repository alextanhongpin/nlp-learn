# -*- coding: utf-8 -*-
import nltk

german_tokenizer = nltk.data.load('tokenizers/punkt/german.pickle')

# Die Küchenuhr by Wolfgang Borchert 
print german_tokenizer.tokenize(u"Sie sahen ihn schon von weitem auf sich zukommen, denn er fiel auf. Er hatte ein ganz altes Gesicht, aber wie er ging, daran sah man, dass er erst zwanzig war. Er setzte sich mit seinem alten Gesicht zu ihnen auf die Bank. Und dann zeigte er ihnen, was er in der Hand trug. Das war unsere Küchenuhr, sagte er und sah sie alle der Reihe nach an, die auf der Bank in der Sonne saßen. Ja, ich habe sie noch gefunden. Sie ist übrig geblieben. Er hielt eine runde tellerweiße Küchenuhr vor sich hin und tupfte mit dem Finger die blau gemalten Zahlen ab.")
