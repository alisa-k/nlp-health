# code to get the most common n-grams
from collections import Counter
import nltk
from nltk import ngrams
from nltk.corpus import stopwords
from operator import itemgetter
import string

# give explanation on why preprocessing prior to identifying ngrams isn't a good idea in this case
def most_common_ngram(text, n):
    # preprocess
    exclude = set(string.punctuation)
    text.lower() # corpus & make lower
    text = ''.join(ch for ch in text if ch not in exclude)
    ngram_counts = Counter(ngrams(text.split(), n))
    print(ngram_counts.most_common(10))
    
    # TODO: figure out how to filter numbers
    stopset = set(stopwords.words('english'))
    top_ngrams_clean = []
    for ngram in ngram_counts:
        if len(set(ngram).intersection(stopset)) == 0:
            top_ngrams_clean.append((ngram,ngram_counts[ngram]))
    # top_ngrams_clean is a list of tuples [((ngram), count), ...]
    # sort ouptut list by second value in tuples (count)
    top_ngrams_clean = sorted(top_ngrams_clean, key=itemgetter(1))[::-1]
    return top_ngrams_clean

if __name__ == "__main__":
    # text = open('big.txt').read()
    #text = nltk.corpus.gutenberg.words('austen-emma.txt')
    text = open('first5.txt').read()
    top_30_ngrams = most_common_ngram(text, 2)[:30]
    for ng in top_30_ngrams: print(ng)

