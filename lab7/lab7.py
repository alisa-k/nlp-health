from nltk import word_tokenize
from nltk.sentiment.util import mark_negation
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.base import TransformerMixin
import pickle as pkl

from unidecode import unidecode
from nltk import word_tokenize
from nltk.classify import NaiveBayesClassifier
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import extract_unigram_feats, mark_negation

import pandas as pd       
import random

###### DATA ###########################################################
# 25000 movie reviews
data = pd.read_csv("labeledTrainData.tsv", header=0, delimiter="\t", quoting=3)
print(data.shape) # (25000, 3) 
print(data["review"][0])         # Check out the review
print(data["sentiment"][0])      # Check out the sentiment (0/1)

sentiment_data = list(zip(data["review"], data["sentiment"]))
random.shuffle(sentiment_data)
 
# 80% for training
train_X, train_y = zip(*sentiment_data[:20000])
# Keep 20% for testing
test_X, test_y = zip(*sentiment_data[20000:])
print("running../")
########################################################################
# SentiWordNet
########################################################################
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn
from nltk import sent_tokenize, word_tokenize, pos_tag
from sklearn.metrics import accuracy_score
 
lemmatizer = WordNetLemmatizer()
 
def penn_to_wn(tag):
    """ Convert between the PennTreebank tags to simple Wordnet tags """
    if tag.startswith('J'):
        return wn.ADJ
    elif tag.startswith('N'):
        return wn.NOUN
    elif tag.startswith('R'):
        return wn.ADV
    elif tag.startswith('V'):
        return wn.VERB
    return None
 
def clean_text(text):
    text = text.replace("<br />", " ")
    return text
 
def swn_polarity(text):
    """ Return a sentiment polarity: 0 = negative, 1 = positive """
    sentiment = 0.0
    tokens_count = 0
    text = clean_text(text)

    raw_sentences = sent_tokenize(text)
    for raw_sentence in raw_sentences:
        tagged_sentence = pos_tag(word_tokenize(raw_sentence))
 
        for word, tag in tagged_sentence:
            wn_tag = penn_to_wn(tag)
            if wn_tag not in (wn.NOUN, wn.ADJ, wn.ADV):
                continue
            lemma = lemmatizer.lemmatize(word, pos=wn_tag)
            if not lemma:
                continue
            synsets = wn.synsets(lemma, pos=wn_tag)
            if not synsets:
                continue
            # Take the first sense, the most common
            synset = synsets[0]
            swn_synset = swn.senti_synset(synset.name())
            sentiment += swn_synset.pos_score() - swn_synset.neg_score()
            tokens_count += 1
    # judgment call ? Default to positive or negative
    if not tokens_count:
        return 0
    # sum greater than 0 => positive sentiment
    if sentiment >= 0:
        return 1
    # negative sentiment
    return 0

#pred_y = [swn_polarity(text) for text in test_X]
#print("SentiwordNet accuracy:")
#print(accuracy_score(test_y, pred_y)) # 0.6518
#unigram_clf = load_clf('classifiers/uni_clf.pkl')
#bigram_clf = load_clf('classifiers/bi_clf.pkl')
#unigram_bigram_clf = load_clf('classifiers/uni_bi_clf.pkl')
########################################################################
# Unigram Classifier
########################################################################
clf = Pipeline([
    ('vectorizer', CountVectorizer(analyzer="word",
                                   tokenizer=word_tokenize,
                                   #tokenizer=lambda text: mark_negation(word_tokenize(text)), 
                                   preprocessor=clean_text,
                                   max_features=10000) ),
    ('classifier', LinearSVC())
])
 
clf.fit(train_X, train_y)
print("Unigram accuracy:")
print(unigram_clf.score(test_X, test_y))
########################################################################
# Bigram Classifier
########################################################################
bigram_clf = Pipeline([
    ('vectorizer', CountVectorizer(analyzer="word",
                                   ngram_range=(2, 2),
                                   tokenizer=word_tokenize, 
                                   # tokenizer=lambda text: mark_negation(word_tokenize(text)),
                                   preprocessor=clean_text,)),
    ('classifier', LinearSVC())
])
 
bigram_clf.fit(train_X, train_y)
print("Bigram accuracy:")
print(bigram_clf.score(test_X, test_y))
########################################################################
# Unigram & Bigram Classifier
########################################################################
unigram_bigram_clf = Pipeline([
    ('vectorizer', CountVectorizer(analyzer="word",
                                   ngram_range=(1, 2),
                                   tokenizer=word_tokenize,
                                   # tokenizer=lambda text: mark_negation(word_tokenize(text)),
                                   preprocessor=clean_text,)),
    ('classifier', LinearSVC())
])

unigram_bigram_clf.fit(train_X, train_y)
print("Unigram & Bigram accuracy:")
print(unigram_bigram_clf.score(train_X, train_y))
########################################################################
# Save / load models
########################################################################
import pickle as pkl

def save_clf(fname, clf):
    with open(fname, 'wb') as f:
        pkl.dump(clf, f)

def load_clf(fname):
    return pkl.load(open(fname, 'rb'))
    with open(fname, 'rb') as f:
        return pkl.load(fname)
########################################################################
save_clf('classifiers/uni_clf.pkl', clf)
save_clf('classifiers/bi_clf.pkl', bigram_clf)
save_clf('classifiers/uni_bi_clf.pkl', unigram_bigram_clf)
########################################################################
unigram_clf = load_clf('classifiers/uni_clf.pkl')
bigram_clf = load_clf('classifiers/bi_clf.pkl')
unigram_bigram_clf = load_clf('classifiers/uni_bi_clf.pkl')




















