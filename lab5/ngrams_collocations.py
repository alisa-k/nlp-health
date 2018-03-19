# http://classes.ischool.syr.edu/ist664/NLPFall2015/LabSessionWeek3.09.16.15.pdf
import nltk
from	nltk	import FreqDist
import re

# emma = nltk.corpus.gutenberg.words('austen-emma.txt')
emmatext	= nltk.corpus.gutenberg.raw('austen-emma.txt') # get raw text
emmatext = open('abstracts.txt').read()
emmatokens = nltk.word_tokenize(emmatext)	 # tokens
emmawords	 = [w.lower()	for w in	emmatokens]

# We're going to look at only the first 300 words
shortwords = emmawords[:100]#[11:110]
print("First 100 words in Emma:\n")
print(shortwords)
print("-" * 50)

# Create a frequency distribution of the words
ndist = FreqDist(shortwords)
nitems = ndist.most_common(30)
print("Frequency distribution of the words:\n")
print([item for item in nitems])
print("-" * 50)

# Define filters - we will apply these later 
def	alpha_filter(w):
    pattern = re.compile('^[^a-z]+$')
    if (pattern.match(w)): return True
    else: return False
stopwords = nltk.corpus.stopwords.words('english')
alphashortwords =	[w for w	in shortwords	if not alpha_filter(w)]
stoppedshortwords	= [w	for w in	shortwords if	not	w in	stopwords]

#############################################################################
# Bigram (Trigram) Frequency Distributions
#############################################################################
# First view the bigrams
shortbigrams = list(nltk.bigrams(shortwords))
print("List of all the bigrams in the first 300 words:\n")
print(shortbigrams)
print("-" * 50)

# Recall collocations
from	nltk.collocations import *

bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(shortwords)
scored = finder.score_ngrams(bigram_measures.raw_freq)
# Print top bigram "scores" (most frequently occuring bigrams)
print("Most frequent bigrams (no filters applied):\n")
for bscore in scored[:30]:
    print(bscore)
print("-" * 50)

# We want to clean this list up now. We will apply our filters to the Finder
finder.apply_word_filter(alpha_filter)
finder.apply_word_filter(lambda	w: w in stopwords)
scored = finder.score_ngrams(bigram_measures.raw_freq)
print("Most frequent bigrams (clean, stopwords removed):\n")
for bscore in scored[:30]:
    print(bscore)
print("-" * 50)

# Notice the "'s". We can change the way we clean the text
#############################################################################
def preprocess(text):
    text = text.lower()
    pattern = r'[a-z]+'
    tokenizer = RegexpTokenizer(pattern)
    tokens = tokenizer.tokenize(text)
    return tokens

# emmatext	= nltk.corpus.gutenberg.raw('austen-emma.txt') # get raw text
emmawords_cleaner = preprocess(emmatext)
shortwords2 = emmawords_cleaner#[9:5008] 

# Lets compare the old list of tokens with the new one
print("="*70 + "\nCleaning Comparison:\n" + "="*70)
print("First method:\n")
print(shortwords[:100])
print("-"*50 + "\n" + "Second method:\n")
print(shortwords2[:100])
print("="*70)

# Now define a new finder, and find new top collocations
finder2 = BigramCollocationFinder.from_words(shortwords2)
finder2.apply_word_filter(lambda w: w in stopwords)
scored = finder2.score_ngrams(bigram_measures.raw_freq)
print("Most frequent bigrams (clean, stopwords removed):\n")
for bscore in scored[:30]:
    print(bscore)
print("-" * 50)

# We can apply another filter, removing where the first word is very short (len <= 2)
finder2.apply_ngram_filter(lambda w1, w2: len(w1) <= 3)
scored = finder2.score_ngrams(bigram_measures.raw_freq)
print("Most frequent bigrams (clean, short 1st words removed):\n")
for bscore in scored[:30]:
    print(bscore)

# Using PMI (?) [works best on very large documents]
# print(finder2.nbest(bigram_measures.pmi, 50))
# print("-" * 50)
    
#############################################################################
#############################################################################
print("\n" + "="*70 + "\nProbabilities\n" + "="*70)
# Get bigrams with "emma" as the first word and the probabilities
emma_occurences = []
for bscore in scored:
    if bscore[0][0] == "emma":
        emma_occurences.append(bscore)
print("Top 15 bigrams that have \"emma\" as the first word:\n")
for i in range(15):
    print(emma_occurences[i])
print("-" * 50)

emma_occurences = [tup for tup in scored if tup[0][0] == "emma"]
print(emma_occurences)

# We can do the same for Trigrams
#############################################################################





















