###############################################################################
# Part 2: BOW
###############################################################################
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import numpy as np

my_documents = ['The movie was about a spaceship and aliens.',
                'I really liked the movie!',
                'Awesome action scenes, but boring characters.',
                'The movie was awful! I hate alien films.',
                'Space is cool! I liked the movie.',
                'More space films, please!']
# CountVectorizer - used to convert a collection of text documents to a matrix of token counts
vectorizer = CountVectorizer()
# Fit transform: Fitting finds the internal parameters of a model that will be 
# used to transform data. Transforming applies the parameters to data. 
# You may fit a model to one set of data, and then transform it on a completely
# different set.
counts = vectorizer.fit_transform(my_documents)
print("\n" + "=" * 50 + "\nBag of Words\n" +"=" * 50)
print("Position of each word in the vector:\n")
print(sorted(vectorizer.vocabulary_.items(), key=lambda x: x[1]))
print("\n"+"-"*70)
print("Vector representations of each sentence in the corpus of docs:\n")
counts_arr = counts.toarray()
for i in range(len(my_documents)):
    print(my_documents[i])
    print(counts_arr[i])
    print()
print("-"*70)   

# Tf-Idf
###############################################################################
# https://s3.amazonaws.com/assets.datacamp.com/production/course_5064/slides/chapter2.pdf
from gensim.corpora.dictionary import Dictionary
from nltk.tokenize import word_tokenize
from gensim.models.tfidfmodel import TfidfModel

# Read in pubmed abstracts 
text = open('abstracts.txt').read()
my_documents = text.split("\n")[:10]
tokenized_docs = [word_tokenize(doc.lower()) for doc in my_documents]

# dictionary contains ids mapped to tokens 
dictionary = Dictionary(tokenized_docs)
print("Mapping of tokens to indices:\n")
print(dictionary.token2id)
print("-"*70)

corpus = [dictionary.doc2bow(doc) for doc in tokenized_docs]
print("Corpus (shows you int representation of the word mapped to frequency):\n")
print(corpus)
print("-"*70)   

print("="*70 + "\nTfidf:\n" + "="*70)
tfidf = TfidfModel(corpus)
def top_tfidf_scores(n):
    '''Words in the document with a high tfidf score occur
    frequently in the document and provide the most information 
    about that specific document.'''
    print(my_documents[n] + "\n")
    # sorted in decreasing order (largest to smallest)
    sorted_by_tfidf = sorted(tfidf[corpus[n]], key = lambda x: x[1])[::-1]
    for i in range(len(sorted_by_tfidf)):
        tokenid = sorted_by_tfidf[i][0]
        score = sorted_by_tfidf[i][1]
        print(str(tokenid) + "\t" + str(dictionary[tokenid]) + "\t" + str(score))

# for each doc, we want to print the relative importance of the terms
for i in range(len(my_documents)):
    top_tfidf_scores(i)
    print("-"*50)
print("-"*70)

# Document Similarity 
###############################################################################
from sklearn.feature_extraction.text import TfidfVectorizer

print("Tfidf document similarity:\n")
tfidf_vect = TfidfVectorizer(min_df=1)
#tfidf = tfidf_vect.fit_transform(my_documents)
#print((tfidf * tfidf.T).A)

tfidf = tfidf_vect.fit_transform(["I'd like an apple",
                                  "An apple a day keeps the doctor away",
                                  "An orange a day keeps the doctor away"])
print((tfidf * tfidf.T).A)
print("Documents 2 and 3 are most similar - with score .8")

# Similarity between words
###############################################################################
import spacy
nlp = spacy.load('en_core_web_md') # python -m spacy download en_core_web_md
tokens = nlp(u'dog cat banana feline')

print("="*70)
print("Finding similarities between tokens:")
print("="*70)
for t1 in range(len(tokens)):
    for t2 in range(t1, len(tokens)):
            print(str(tokens[t1]) + ", " + 
                  str(tokens[t2]) + ": " + 
                  str(tokens[t1].similarity(tokens[t2])))
