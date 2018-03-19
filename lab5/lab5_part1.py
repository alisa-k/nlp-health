# Get your pubmed abstracts 
from Bio import Entrez
import csv 

def searchPubmed(query, num_of_results):
    #Pubmed needs your email to warn you for searching for too many articles at once
    Entrez.email = 'ham2026@med.cornell.edu' 
    if num_of_results > 20:
        raise ValueError('Search for less results! - Change the value in the num_of_results in searchPubMed function')
    else: 
        handle = Entrez.esearch(db='pubmed', 
                            sort='relevance', 
                            retmax= num_of_results,
                            retmode='text', # 'xml' , 'text'
                            term=query)
        #print(handle.url)
        results = Entrez.read(handle)
    listOfPMID = results.get('IdList')
    abstractSearched = []
    for each in listOfPMID: 
        handle = Entrez.efetch(db="pubmed", id=each ,
                       rettype="xml", retmode="text", term = 'heart attack')
        records = Entrez.read(handle)
        abstractlist = records['PubmedArticle'][0]['MedlineCitation']['Article']['Abstract']['AbstractText']
        if len(abstractlist) > 1: 
            abstract = ''
            for eachsection in abstractlist: 
                abstract += str(eachsection)
            abstractSearched.append(abstract)
        else: 
            abstractSearched.append(abstractlist[0])
    return abstractSearched

def list_to_txt(listOfAbstracts, fileName):
    f = open(str(fileName) + '.txt', 'w')  
    for item in listOfAbstracts: 
        f.write("%s\n" % item)
    f.close()
    print('list converted to .txt file')


## Below is where you would change the query
searchquery =searchPubmed("Natural Language Processing", 10)
list_to_txt(searchquery, 'abstractsLab5')


###############################################################################
# Part 1: n-grams
###############################################################################
import nltk
from nltk import ngrams
from collections import Counter
from nltk.corpus import stopwords
from operator import itemgetter
import string

# Finding the most common ngrams (without preprocessing)
############################################################
#text = """I need to write a program in, a program in NLTK that breaks a corpus (a large
#collection of txt files) into unigrams, bigrams, trigrams, fourgrams and 
#fivegrams. I need to write a program in NLTK that breaks a corpus"

text = open('abstractsLab5.txt').read()
text.lower()
tokens = nltk.word_tokenize(text)
# bigrams and trigrams are generator objects
bigrams = ngrams(tokens,2)
trigrams = ngrams(tokens,3)
quadrigrams = ngrams(tokens,4)

print("Most common bigrams:\n")
for key, value in Counter(bigrams).most_common()[:10]:
    print(str(value) + "\t" + str(key))
print()
print("Most common trigrams:\n")
for key, value in Counter(trigrams).most_common()[:10]:
    print(str(value) + "\t" + str(key))
print()
print("Most common quadrigrams:\n")
for key, value in Counter(quadrigrams).most_common()[:10]:
    print(str(value) + "\t" + str(key))

# Finding Conditional Frequency Distributions
############################################################
from nltk.corpus import brown
cfreq_brown_2gram = nltk.ConditionalFreqDist(nltk.bigrams(brown.words(categories="government")))
brown_trigrams = nltk.trigrams(brown.words(categories="government"))
condition_pairs = (((w0, w1), w2) for w0, w1, w2 in brown_trigrams)
cfd_brown = nltk.ConditionalFreqDist(condition_pairs)
print(cfd_brown[("United", "States")].items())
            
cfreq_brown_2gram = nltk.ConditionalFreqDist(nltk.bigrams(tokens))
brown_trigrams = nltk.trigrams(tokens)
condition_pairs = (((w0, w1), w2) for w0, w1, w2 in brown_trigrams)
cfd_brown = nltk.ConditionalFreqDist(condition_pairs)
print(cfd_brown[("natural", "language")].items())















