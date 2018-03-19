#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 22:52:59 2018

@author: hannah
"""
#Intro: Preprocessing - simple examples
from nltk.tokenize import RegexpTokenizer
from nltk import word_tokenize
#lowercase all words 
def wordlowercase(text):
    return (text.lower())
text = "I am a person. Do you know what time it is?"
textlower = wordlowercase(text)
print(textlower)


# look at nltk stop list 
from nltk.corpus import stopwords 
stoplist = set(stopwords.words('english'))
print(stoplist)

#remove stop words 
tokens = word_tokenize(textlower)
stoplist = set(stopwords.words('english'))
cleanwordlist = [word for word in tokens if word not in stoplist]
print(cleanwordlist)

# remove punctuation & numbers
tokenizer = RegexpTokenizer(r'[a-z]+') #keeps only lowercase words 
tokens = tokenizer.tokenize(textlower)
print(tokens)

# notice the difference between tokenizing with 
# all lowercase (textlower) versus a mixed case (text)
tokens2 = tokenizer.tokenize(text)
print(tokens2)

import re
#how to get just the words & not tokenize 
lowerPattern = r'[a-z]+'
capitalPattern = r'[A-Z]\w*'

print(re.findall(lowerPattern,text))
print(re.findall(capitalPattern,text))


# WordCloud  - have to install with pip install wordcloud
from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
import random
from nltk.corpus import stopwords 

from wordcloud import WordCloud, STOPWORDS

text = 'all your base are belong to us all of your base base base'
wordcloud = WordCloud(font_path='/Library/Fonts/Verdana.ttf',
                      relative_scaling = 1.0,
                      # stopwords is a set or space-separated string
                      stopwords = {'to', 'of'}, #set(stopwords.words('english')), 
                      width = 1600, 
                      height =800
                      ).generate(text)

#wordcloud = WordCloud().generate(text)
plt.figure(figsize=(10,5), facecolor = 'k')
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

from nltk import word_tokenize 
text = "I am a person. Do you know what time it is? The boy jumped for joy! \
It is 9:30 am"
wordlist = word_tokenize(text)
###takes a list 
#find words that end in 'ed'
edEnding = [w for w in wordlist if re.search('ed$', w)]
print(edEnding)

import re
text = 'my birthday is 02/21/18'
date = r'[0-9][0-9]/[0-9][0-9]/[0-9][0-9]'
print(re.findall(date,text))


re.split(r'[ \t\n]+', text)
# Write a pattern to match sentence endings: sentence_endings
sentence_endings = r"[.?!]"

# Split my_string on sentence endings and print the result
print(re.split(sentence_endings, text))

# Find all capitalized words in my_string and print the result
capitalized_words = r"[A-Z]\w+"
print(re.findall(capitalized_words, text))

# Split my_string on spaces and print the result
spaces = r"\s+"
print(re.split(spaces, text))

# Find all digits in my_string and print the result
digits = r"\d+"
print(re.findall(digits, text))


#customized stop words removal 
stop_words = set(["am", "it", "is", "a"])
line = """hi this is foo. bye"""
print ("")
print ("--------Customized stopword removal---------")
noStopWords = " ".join(word for word in text.split() if word not in stop_words)
print(noStopWords)

# nltk stop word removal
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))
print ("")
print ("--------Stop word removal from raw text---------")
noStopWordsNLTK = " ".join([i for i in text.lower().split() if i not in stop])
print(noStopWordsNLTK)

#advanced regex - look aheads/look behinds - from textbook
text = "I play on playground. It is the best ground."

positivelookaheadobjpattern = re.findall(r'play(?=ground)',text,re.M | re.I)
print ("Positive lookahead: " + str(positivelookaheadobjpattern))
positivelookaheadobj = re.search(r'play(?=ground)',text,re.M | re.I)
print ("Positive lookahead character index: "+ str(positivelookaheadobj.span()))

possitivelookbehindobjpattern = re.findall(r'(?<=play)ground',text,re.M | re.I)
print ("Positive lookbehind: " + str(possitivelookbehindobjpattern))
possitivelookbehindobj = re.search(r'(?<=play)ground',text,re.M | re.I)
print ("Positive lookbehind character index: " + str(possitivelookbehindobj.span()))

negativelookaheadobjpattern = re.findall(r'play(?!ground)', text, re.M | re.I)
print ("Negative lookahead: " + str(negativelookaheadobjpattern))
negativelookaheadobj = re.search(r'play(?!ground)', text, re.M | re.I)
print ("Negative lookahead character index: " + str(negativelookaheadobj.span()))

negativelookbehindobjpattern = re.findall(r'(?<!play)ground', text, re.M | re.I)
print ("negative lookbehind: " + str(negativelookbehindobjpattern))
negativelookbehindobj = re.search(r'(?<!play)ground', text, re.M | re.I)
print ("Negative lookbehind character index: " + str(negativelookbehindobj.span()))



