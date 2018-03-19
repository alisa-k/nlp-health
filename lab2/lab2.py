 # -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 12:18:58 2017

@author: ham2026

This contains python 3.x version of the textbook code found at: 
    https://nbviewer.jupyter.org/github/jalajthanaki/NLPython/blob/master/ch2/2_1_Basic_corpus_analysis.html

This lab works best by copying and pasting the code from the file into the shell 
or the "IPython console" on the bottom right of the screen. 

to reset your variable type "%reset" in the console 
"""
##################### data sources ########################################

import os 

#os.getcwd() #return current directory 

# Option 1: from a .txt file (notes.txt)
file = open('notes.txt', 'r') #reads and removes all unreadable characters coded with utf-8

#read the file 
contents = file.read()
#close the file you opened above
file.close()
# manipulate your file 
#print(contents)

# Option 2: from .csv file to a pandas dataframe (MIMIC)
import pandas as pd 
import nltk 
file = "NOTEEVENTS.csv"
num_of_rows = 100
df = pd.read_csv(file, nrows = num_of_rows)
df['tokenized_text'] = df['TEXT'].apply(nltk.word_tokenize) 
tokenizedTextList = df['tokenized_text'].tolist()

# Option 3: Webpage Data (lab1 - wikipedia)
from urllib import request 
from bs4 import BeautifulSoup
from nltk import word_tokenize

def text_from_webpage(webpage):
    #open the webpage and read it 
    html = request.urlopen(webpage).read().decode('utf8')
    # convert the text from html to plain text 
    raw = BeautifulSoup(html, 'html.parser').get_text()
    #tokenize each word 
    tokens = word_tokenize(raw)
    return tokens  
webpagetoken = text_from_webpage("https://en.wikipedia.org/wiki/Natural_language_processing")

# Option 4: From pubmed - see separate file 

# Option 5: assigning text to a variable directly 

notes = '''Pt. X: 28 yr old female with a history of abdominal pain, mid epigastric, worse when eating, and lying down after eating, 
and greasy foods. Also has pain when not eating, nausea, vomiting- gastric content, no blood or coffee ground 
emesis. Now qd x five months, has lost 145--->139/3 weeks. BM brown, blood streaking occasionally.  chronic 
constipation WOrse x 4 months,  5 days,  uses laxatives qd. and lower abdominal pain.   ROS: Headache bilaterally, 
pressure like around menses N  visual acuity changes, Y corrective lenses, no fever or chills, N nasal  congestion,  no 
pruritic eyes, N  cough N abdominal pain N diarrhea N constipation,  no urinary or  bowel incontinence,  no heat or cold 
intolerance, no skin changes.  Nutrition:  Wt change as above Special  diet  none regular exercise;  occ push-up, no 
aerobic Medicines: laxative   ALLERGY: NKDA HABITS: cig N   N  ETOH occasional  Illicit drug  N PMHx: as above  PSHx: 
C-section 10 yrs ago PSYCH Hx:  	Depression N     Anxiety N 	N sleep disturbance,  no anhedonia  good appetite  
NO SI/HI OBhx/sexual history  P1001   LMP 12/13/09  regular    last PAP 2010  nl   GC / N CT /HSV N/Syphilis N  HIV 
negative 10/2009 Pending   sexually active without condoms one partner FHx.  Father age 60s asthma, DM    	Mother 
age 50s  HTN No CA, CVA,   MGF  age 80s MI SHx:  Lives with daughter     Employment none      Education: college 
Vaccines:  TD  none    Flu  N/A    Pneumovax n/a 	PPD  not done in the US >10yrs PE see intake form Wt 139    BP 
151/66   P 63 		  A/P    	 1.	Dyspepsia/GERD Protonix x 3 months Life style changes 2.	Chronic 
constipation with laxative abuse Dietary change encouraged Psyllium/miralax for initial use to be weaned  Fluid intake 
and exercise 3.	Anemia in a menstruating women Will check again But will consider endoscopic examination  5.  
HM:   pt to bring record of td vaccine RTC in 4 months  Doctor X MD 
'''
############### Exploring Corpus in NLTK ##################################
#Import avaliable corpus from NLTK
import nltk 

# brown corpus a corpora categorized by genre (news, )
from nltk.corpus import brown as cb #cb is an abbreviation for the brown corpus
from nltk.corpus import gutenberg as cg 

#print all directories inside the brown corpus
print (dir(cb)) 

#list all the topics in the brown corpus
print (cb.categories())

###try to get the categories of the gutenberg corpora (named cg)

#name of brown corpus file chunks
print (cb.fileids())

#first 20 words of brown corpus
print (cb.words()[0:20])

#20 words of news category starting with the 10th word
print(cb.words(categories='news')[10:30])

###try to get the first 20 words for the humor category 


#extract words from data file 'cg22'
print (cb.words(fileids=['cg22']))

#Part of Speech tags for brown corpus
print (cb.tagged_words()[0:10])

### try to find the tagged words for the category humor 


##try the below 
#cb.concordance(‘jury’) 

#Brown corpus - raw text without tags
raw_textca01 = nltk.Text(cb.words('ca01')) #converts the categorized corpora into raw text 
print (raw_textca01)

#check how many times a word is in a corpus
raw_textca01.concordance("jury")

raw_textca01.concordance("recent")

#Raw data from brown corpus 
raw_content = cb.raw("ca01")
print (raw_content)
# print (raw_content[0:1000]) # print 1000 words

#Look at files inside the gutenberg corpus
print (cg.fileids())

#look at the first 1000 words from the burgess-busterbrown.txt file in the gutenberg corpus

raw_content_cg = cg.raw("burgess-busterbrown.txt")
print (raw_content_cg[0:1000])

# look at the words from the burgess-busterbrown.txt file in the gutenberg 
wordsBurgess = cg.words("burgess-busterbrown.txt")
print(wordsBurgess)
# look at the sentences from the burgess-busterbrown.txt file in the gutenberg
sentsBurgess = cg.sents("burgess-busterbrown.txt")
print(sentsBurgess)

# Calculate the number of characters in the corpus file id 'burgess-busterbrown.txt'
num_chars_cg =len(raw_content_cg)
print (num_chars_cg)

#Calculate the number of words in the corpus file id 'burgess-busterbrown.txt'
num_words = len(wordsBurgess)
print (num_words)

#Calculate the number of sentences in the corpus file id 'burgess-busterbrown.txt'
sentsBurgess = cg.sents("burgess-busterbrown.txt")
num_sents = len(sentsBurgess)
print (num_sents) 

# frequency distribution for corpus
from nltk.book import *
import nltk
from nltk import FreqDist

# find the frequency distribution of words in the text and most common words 
fdist1 = FreqDist(wordsBurgess)
### try the values below and see what values you get 
#fdist2 = FreqDist(raw_content_cg)
#fdist3 = FreqDist(sentsBurgess)
print (fdist1)
print (fdist1.most_common(50))


#############################################################################
####### load your own single file to tokenize with nltk.Text() ##############

#tokenize from a data string 
import nltk 
from nltk.tokenize import sent_tokenize, word_tokenize

# tokenize from a single data string 
file = open("notes.txt", "r") # reads as bytes
#reads and removes all unreadable characters coded with utf-8

#read the file 
contents = file.read()
#close the file you opened above
file.close()
#spilt file by words 
#text = contents.split()
text = word_tokenize(contents[0:100])
#covert file to nltk.Text object 
fileText = nltk.Text(text)

vocabset = fileText.vocab()

print (len(contents) )
print(type(contents))
print(contents)
print(type(text))
print(text)

print(type(fileText))
print(fileText)

phrasesFile = sent_tokenize(contents)
wordsFile = word_tokenize(contents)
vocablist = set(word_tokenize(contents))
print(phrasesFile[:5])
print(wordsFile[:30])

fdistweb = FreqDist(wordsFile) #this creates a frequency distribution of all words 
print(fdistweb)
print("\n")
print(fdistweb.most_common(100))

######Load your own corpus from notes.txt file - with PlaintextCorpusReader ########
    # harder to manipulate 

# tokenize from a directory of files see http://www.nltk.org/_modules/nltk/corpus/reader/plaintext.html
from nltk.corpus import PlaintextCorpusReader

#this is the location of corpus folder 
corpus_root = os.path.expanduser("~/Documents/NLPHealth/WCM-Course/corpusFolder")
#create a corpus of all files in the folder 
newcorpus = PlaintextCorpusReader(corpus_root, '.*')

note1words = newcorpus.words("notes.txt")
#if there is more than 1 notes file 
allwords = newcorpus.words()
allparagraphs = newcorpus.paras()
allsents = newcorpus.sents()

print(type(allwords))
print("\nwords\n", allwords)
print("\nparagraphs\n", allparagraphs)
print("\nsentences\n", allsents)
#print(contents)

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








'''
from nltk.corpus import treebank as tb 

print(dir(tb))

print (tb.fileids())

print (tb.words()[0:20])

print (tb.words(fileids=['wsj_0003.mrg']))

print (tb.tagged_words()[0:10])

raw_text2 = nltk.Text(tb.words('wsj_0003.mrg'))
print (raw_text2)
print(raw_text2.collocations())

raw_content2 = tb.raw('wsj_0030.mrg')
print(raw_content2)

print(tb.words('wsj_0030.mrg'))

#print(tb.sent())
'''



