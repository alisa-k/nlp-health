from sklearn.cluster import KMeans
from sklearn.decomposition import PCA, TruncatedSVD
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
import numpy as np

from random import shuffle

#documents = ["Human machine interface for lab abc computer applications",
#             "A survey of user opinion of computer system response time",
#             "The EPS user interface management system",
#             "System and human system engineering testing of EPS",
#             "Relation of user perceived response time to error measurement",
#             "The generation of random binary unordered trees",
#             "The intersection graph of paths in trees",
#             "Graph minors IV Widths of trees and well quasi ordering",
#             "Graph minors A survey"]

documents = []
with open("data/ear.txt", "r") as f:
    documents.extend(f.read().splitlines())
with open("data/brain.txt", "r") as f:
    documents.extend(f.read().splitlines())
with open("data/eye.txt", "r") as f:
    documents.extend(f.read().splitlines())
shuffle(documents)

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

true_k = 3
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)

print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print("Cluster %d:" % i)
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind])
    print()

