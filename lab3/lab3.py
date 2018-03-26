# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 16:13:27 2017

@author: ham2026

"""

############### Ways to Tokenize ##########################################

s = '''Hello everyone, this is NLP Health Course!    
The class time is 5:00pm to 6:30pm.''' 
#the triple quotes creates the newline to be read at \n

print(s.split())

from nltk.tokenize import word_tokenize 
print(word_tokenize(s))

from nltk.tokenize import regexp_tokenize, wordpunct_tokenize, blankline_tokenize 
print(regexp_tokenize(s, pattern='\w+'))

print(regexp_tokenize(s, pattern='\d+'))

print(wordpunct_tokenize(s))

print(blankline_tokenize(s))

######################Stemmers #########################
from nltk.stem import PorterStemmer 
port = PorterStemmer() #create object of the Porterstemmer 

from nltk.stem import LancasterStemmer 
lanc = LancasterStemmer()

from nltk.stem import SnowballStemmer 
snowb = SnowballStemmer('english')
print ("----------Stemming with Porter----------")
print(port.stem('eating'))
print(port.stem('shopping')) 
print(port.stem('unexpected'))
print(port.stem('disagreement')) 
print(port.stem('agreement'))
print(port.stem('quirkiness')) 
print(port.stem('historical'))
print(port.stem('canonical')) 
print(port.stem('eating'))
print(port.stem('shopping')) 
print(port.stem('happiness'))
print(port.stem('unkind')) 
print(port.stem('dogs'))
print(port.stem('expected')) 

print ("----------Stemming with Lancaster ----------")
print(lanc.stem('eating'))
print(lanc.stem('shopping')) 
print(lanc.stem('unexpected'))
print(lanc.stem('disagreement')) 
print(lanc.stem('agreement'))
print(lanc.stem('quirkiness')) 
print(lanc.stem('historical'))
print(lanc.stem('canonical')) 
print(lanc.stem('eating'))
print(lanc.stem('shopping')) 
print(lanc.stem('happiness'))
print(lanc.stem('unkind')) 
print(lanc.stem('dogs'))
print(lanc.stem('expected')) 

print ("----------Stemming with Snowball ----------")
print(snowb.stem('eating'))
print(snowb.stem('shopping')) 
print(snowb.stem('unexpected'))
print(snowb.stem('disagreement')) 
print(snowb.stem('agreement'))
print(snowb.stem('quirkiness')) 
print(snowb.stem('historical'))
print(snowb.stem('canonical')) 
print(snowb.stem('eating'))
print(snowb.stem('shopping')) 
print(snowb.stem('happiness'))
print(snowb.stem('unkind')) 
print(snowb.stem('dogs'))
print(snowb.stem('expected')) 


# how to stem a sentence 
sentence = 'gaming, the gamers play games'
words = word_tokenize(sentence)
for word in words: 
    print(word + ':' + port.stem(word))


'''
from polyglot.text import Text, Word
def polyglot_stem():
    print ("\nDerivational Morphemes using polyglot library")
    for w in words_derv:
        w = Word(w, language="en")
        print("{:<20}{}".format(w, w.morphemes))
    print( "\nInflectional Morphemes using polyglot library")
    for w in word_infle:
        w = Word(w, language="en")
        print("{:<20}{}".format(w, w.morphemes))
    print ("\nSome Morphemes examples using polyglot library")
    for w in word_infle:
        w = Word(w, language="en")
        print("{:<20}{}".format(w, w.morphemes))
'''

####################Lemmatization #########################
from nltk.stem import WordNetLemmatizer 
wordlemma = WordNetLemmatizer() #create object of the WordNetLemmatizer 
print ("----------Word Lemmatization----------")
print (wordlemma.lemmatize('cars'))
print (wordlemma.lemmatize('walking',pos='v'))
print (wordlemma.lemmatize('meeting',pos='n'))
print (wordlemma.lemmatize('meeting',pos='v'))
print (wordlemma.lemmatize('better',pos='a'))
print (wordlemma.lemmatize('is',pos='v'))
print (wordlemma.lemmatize('funnier',pos='a'))
print (wordlemma.lemmatize('expected',pos='v'))
print (wordlemma.lemmatize('fantasized',pos='v'))

## Lemmatize a sentence 
text = """Stemming is funnier than a bummer says the sushi loving computer scientist.
She really wants to buy cars. She told me angrily.
It is better for you. Man is walking. We are meeting tomorrow."""


ADJ, ADJ_SAT, ADV, NOUN, VERB = 'a', 's', 'r', 'n', 'v'
# Pos = verb
print ("\nVerb lemma")
print (" ".join([wordlemma.lemmatize(i,pos="v") for i in text.split()]))
# Pos =  noun
print ("\nNoun lemma")
print (" ".join([wordlemma.lemmatize(i,pos="n") for i in text.split()]))
# Pos = Adjective
print ("\nAdjective lemma")
print (" ".join([wordlemma.lemmatize(i, pos="a") for i in text.split()]))
# Pos = satellite adjectives
print ("\nSatellite adjectives lemma")
print (" ".join([wordlemma.lemmatize(i, pos="s") for i in text.split()]))
print ("\nAdverb lemma")
# POS = Adverb
print (" ".join([wordlemma.lemmatize(i, pos="r") for i in text.split()]))
    
import nltk
from nltk import CFG
from nltk.tree import *
# from pycorenlp import StanfordCoreNLP
from collections import defaultdict

# Part 1: Define a grammar and generate parse result using NLTK
def definegrammar_pasrereult():
    Grammar = nltk.CFG.fromstring(""" 
    S -> NP VP 
    PP -> P NP 
    NP -> Det N | Det N PP | 'I' 
    VP -> V NP | VP PP 
    Det -> 'an' | 'my' 
    N -> 'elephant' | 'pajamas' 
    V -> 'shot' | 'wore'
    P -> 'in' 
    """)
    sent = "I shot an elephant".split()
    #sent = "I wore my pajamas".split()
    parser = nltk.ChartParser(Grammar)
    trees = parser.parse(sent)
    for tree in trees:
        print(tree)

# Part 2: Draw the parse tree
def draw_parser_tree():
    dp1 = Tree('dp', [Tree('d', ['the']), Tree('np', ['dog'])])
    dp2 = Tree('dp', [Tree('d', ['the']), Tree('np', ['cat'])])
    vp = Tree('vp', [Tree('v', ['chased']), dp2])
    tree = Tree('s', [dp1, vp])
    print(tree)
    print(tree.pformat_latex_qtree())
    tree.pretty_print()


# Part 3: Stanford parser wrapper library "pycorenlp"
# you need to install pycorenlp as well as you need to download stanford-corenlp-full-* from standford corenlp website.
def stanford_parsing_result():
    text =""" I shot an elephant. The dog chased the cat. School go to boy. """
    nlp = StanfordCoreNLP('http://localhost:9000')
    res = nlp.annotate(text, properties={
        'annotators': 'tokenize,ssplit,pos,depparse,parse',
        'outputFormat': 'json'
    })
    print(res['sentences'][0]['parse'])
    print(res['sentences'][2]['parse'])


if __name__ == "__main__":
    print ("\n--------Parsing result as per defined grammar-------")
    definegrammar_pasrereult()
    print ("\n--------Drawing Parse Tree-------")
    draw_parser_tree()
    print ("\n--------Stanford Parser result------")
    stanford_parsing_result()



# -*- coding: utf-8 -*-

