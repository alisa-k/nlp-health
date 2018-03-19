import nltk
import re
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from nltk.corpus import gutenberg as cg


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
    freqDist = nltk.FreqDist(cleanwordlist)
    rare_words_len = int(len(cleanwordlist) * 0.05)
    rare_words = list(freqDist.keys())[-rare_words_len:]
    print(rare_words)
    after_rare_words= [word for word in cleanwordlist if word not in rare_words]
    return after_rare_words

f = open('../lab2/notes.txt', 'r')
contents = f.read()
f.close()

raw_content = cg.raw("burgess-busterbrown.txt")
sentence = 'this is just a test2324!!!q234 asdlfijasdlkfj jeans t-shirt aisdf hi hello hey jeans lion lion lion lion lion lion ladf alsdfkj asdf' 
preprocess(contents)
