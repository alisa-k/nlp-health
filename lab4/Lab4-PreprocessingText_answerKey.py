# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 16:30:34 2017

@author: ham2026

Lab on preprocessing text - lab 4 
"""
#####################################################################
# Part A: Wordcloud on mimic data 
import pandas as pd 
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords 
df = pd.read_csv('noteevents_top10.csv', nrows = 10)
dfDischarge = df.loc[df['CATEGORY']== 'Discharge summary'] 
#print(df)
notesList = dfDischarge["TEXT"].tolist()

# look at your file in excel 
dfDischarge.to_csv('first5.csv')
# OR look at your file in notepad
f = open('first5.txt', 'w')
for pt_note in notesList: 
    f.write("-"*80 + "\n")
    f.write(pt_note)
f.close()

# preprocesses each note separately 
# processedNotesList1 = lowercase, no punct, no numbers or symbols 
processedNotesList1 = []
for text in notesList: 
    textlower = text.lower() #lowercase
    tokenizer = RegexpTokenizer(r'[a-z]+') #tokenize & keep only lowercase words 
    tokens = tokenizer.tokenize(textlower)
    processedNotesList1.append(tokens)
#processedNotesList1 is a list of lists 

#combine all preprocessed notes into one big list of words for further analysis
allNotesWords1 = []
for sublist in processedNotesList1:
    for item in sublist:
        allNotesWords1.append(item)

# WordCloud  - have to install with pip install wordcloud
from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
import random 
from wordcloud import WordCloud, STOPWORDS

def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist,wordfreq))

freqDict = wordListToFreqDict(allNotesWords1)
wordcloud = WordCloud(font_path='/Library/Fonts/Verdana.ttf',
                      relative_scaling = 1.0,
                      width = 1600, 
                      height =800
                      ).generate_from_frequencies(freqDict)

#wordcloud = WordCloud().generate(text)
print('\n no punctuation, no lowercase, no symbols/numbers \n----------------------------------------')
plt.figure(figsize=(20,10), facecolor = 'k')
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig('word_cloud.png')
plt.show()

### 
#Now remove stop words
# processedNotesList2 = no stopwords, lowercase, no punct, no numbers or symbols 
processedNotesList2 = []
for text in notesList: 
    textlower = text.lower() #lowercase
    tokenizer = RegexpTokenizer(r'[a-z]+') #tokenize & keep only lowercase words 
    tokens = tokenizer.tokenize(textlower)
    stoplist = set(stopwords.words('english'))
    #remove stopwords 
    cleanwordlist = [word for word in tokens if word not in stoplist]
    processedNotesList2.append(cleanwordlist)
#processedNotesList2 is a list of lists 

#combine all preprocessed notes into one big list of words for further analysis
allNotesWords2 = []
for sublist in processedNotesList2:
    for item in sublist:
        allNotesWords2.append(item)

freqDict2 = wordListToFreqDict(allNotesWords2)
wordcloud = WordCloud(font_path='/Library/Fonts/Verdana.ttf',
                      relative_scaling = 1.0,
                      stopwords = set(stopwords.words('english')), #{'to', 'of'} # set or space-separated string
                      width = 1600, 
                      height =800
                      ).generate_from_frequencies(freqDict2)

#wordcloud = WordCloud().generate(text)
print('\nno stopwords, no punctuation, no lowercase, no symbols/numbers \n----------------------------------------')
plt.figure(figsize=(20,10), facecolor = 'k')
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig('word_cloud.png')
plt.show()


# one simple formula to preprocess 
def preprocess(text):
    text = text.lower()
    # remove just punctuation
    # tokenizer = RegexpTokenizer(r'\w+')
    
    # remove punctuation & numbers
    tokenizer = RegexpTokenizer(r'[a-z]+')
    tokens = tokenizer.tokenize(text)
    # remove stop words
    stoplist = set(stopwords.words('english'))
    cleanwordlist = [word for word in tokens if word not in stoplist]
    # remove rare words
    #freqDist = nltk.FreqDist(cleanwordlist)
    #rare_words_len = int(len(cleanwordlist) * 0.05)
    #rare_words = list(freqDist.keys())[-rare_words_len:]
    #print(rare_words)
    #after_rare_words= [word for word in cleanwordlist if word not in rare_words]
    return " ".join(cleanwordlist)

################################################################
## Part B: Regex - looking for patterns in text 
    
# basics of regex 
import re 
from nltk.tokenize import word_tokenize

tokenizedList = []
for each in notesList: 
    tokenizedList.append(word_tokenize(each)) 
    
#find all numbers in the clinical notes
number3digits= r"[0-9]{1,3}\s"
# the loop below uses re.findall on each note separately
for i, each in enumerate(notesList):
    print('Note %d: ' % (i+1))
    print(re.findall(number3digits,each, re.M | re.I)) #re.I ignores case

#find age with new formula 
#agePattern = r"\d{2}\s?(?=(?:years old|yo|yr old|y o|yrs old|year old)(?!\s?son|\s?daughter|\s?kid|\s?child))"
agePattern = r'(\d{2}\s)(years old|yo|yr old|y o|yrs old|year old)'
for i, each in enumerate(notesList):
    print('Note %d has age: ' %(i+1))
    print(re.findall(agePattern,each, re.M |re.I))


## find admission date - change to regex! 
admissionPattern = 'Admission Date: [**2124-7-21**]' 
admissionPattern = r'Admission Date\:\s\s\[\*\*\d{4}-\d{1,2}-\d{1,2}\*\*\]' 

for i, each in enumerate(notesList): 
    print('Note %d: ' %(i+1))
    print(re.findall(admissionPattern, each, re.M))


# create a preprocessed list of notes
processedList = []
for each in notesList: 
    processedList.append(preprocess(each))

################################################################
## Part C: tfidf 
# this will compare 
import math
from textblob import TextBlob as tb

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

bloblist = [tb('''"""'''+doc+'''"""''') for doc in processedList]
for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:3]:
        print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
