import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA, TruncatedSVD
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline


### For the purposes of this example, we store feature data from our
### dataframe `df`, in the `f1` and `f2` arrays. We combine this into
### a feature matrix `X` before entering it into the algorithm.
# get the data, divide it into training and testing data sets
#df = pd.read_csv('multi_class_data.csv')
##set up colors per clusters using a dict
#cluster_colors = {0: '#1b9e77', 1: '#d95f02', 2: '#7570b3'}
#cluster_names = df.label.map({'breast':0, 'foot':1, 'ear':2})

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
with open("ear.txt", "r") as f:
    documents.extend(f.read().splitlines())
with open("brain.txt", "r") as f:
    documents.extend(f.read().splitlines())
with open("eye.txt", "r") as f:
    documents.extend(f.read().splitlines())

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
    for ind in order_centroids[i, :3]:
        print(' %s' % terms[ind])
    print()

#centers2D = pca.transform(kmeans.cluster_centers_)
#colors = df.apply(lambda row: cluster_colors[row.label], axis=1)
#
#ax = df.plot(kind='scatter', alpha=0.1, s=300, c=colors)
#plt.show()
#plt.hold(True)
#plt.scatter(centers2D[:,0], centers2D[:,1], 
#            marker='x', s=200, linewidths=3, c='r')
#plt.show() 