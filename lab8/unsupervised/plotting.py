from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans

import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

import matplotlib.pyplot as plt

from random import shuffle
import string
import re

# create our own set of documents 
documents = []
with open("data/eye.txt", "r") as f:
    documents.extend(f.read().splitlines())
with open("data/brain.txt", "r") as f:
    documents.extend(f.read().splitlines())
shuffle(documents)

# transform our text into vectors & transform with tfidf 
pipeline = Pipeline([
    ('vect', TfidfVectorizer()),
    ('tfidf', TfidfTransformer()),
])        
X = pipeline.fit_transform(documents).todense()

# set a k
true_k = 2

# fit our kmeans model to our transformed data
kmeans_model = KMeans(n_clusters=true_k)
kmeans_model.fit(X)

# reduce our data to 2 dimensions so we can visualize it  
pca = PCA(n_components=2).fit(X)
data2D = pca.transform(X)
centers2D = pca.transform(kmeans_model.cluster_centers_)

plt.scatter(data2D[:,0], data2D[:,1], c=kmeans_model.labels_)
plt.scatter(centers2D[:,0], centers2D[:,1], 
            marker='x', s=200, linewidths=3, c='r')
plt.show()   

# print top terms
vectorizer = TfidfVectorizer(stop_words='english')
X_2 = vectorizer.fit_transform(documents)
kmeans_model.fit(X_2)

print("Top terms per cluster:")
order_centroids = kmeans_model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
#terms = pipeline.named_steps['vect'].get_feature_names()
for i in range(true_k):
    print("Cluster %d:" % i)
    for ind in order_centroids[i, :5]:
        print(' %s' % terms[ind])
    print()