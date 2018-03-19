import string
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import re

def preprocess(sentence):
    sentence = sentence.lower()
    pattern = r'[a-z]+'
    #pattern = r'\w+'
    tokenizer = RegexpTokenizer(pattern)
    tokens = tokenizer.tokenize(sentence)
    stop_words = stopwords.words('english')
    filtered_words = [w for w in tokens if not w in stop_words]
    return " ".join(filtered_words)

sentence = "At eight o'clock on Thursday _morning_ Mr. Arthur's didn't 8th feel very good. French-Fries"
print(preprocess(sentence))