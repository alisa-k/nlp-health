import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

from sklearn import datasets, linear_model
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

# get the data, divide it into training and testing data sets
df = pd.read_csv('data/binary_classification_data.csv')
df['label_num'] = df.label.map({'breast':0, 'foot':1})

X = df.abstract
y = df.label_num
# does a 75/25 split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

#learn training data vocabulary, then use it to create a document-term matrix
vect = CountVectorizer()
X_train_dtm = vect.fit_transform(X_train)
X_test_dtm = vect.transform(X_test)

# fit a model
lm = linear_model.LinearRegression()
model = lm.fit(X_train_dtm, y_train)
predictions = lm.predict(X_test_dtm)
#lr_results = pd.DataFrame(list(zip(X_test, y_test, predictions)),
#              columns=['abstract','expected', 'predicted'])
print("Score:", model.score(X_test_dtm, y_test))

##### BINARY CLASSIFIER #####
from sklearn import tree
from sklearn import metrics

clf = tree.DecisionTreeClassifier(criterion='entropy')
clf.fit(X_train_dtm, y_train)
y_pred_class = clf.predict(X_test_dtm)
print(metrics.accuracy_score(y_test, y_pred_class))
results = pd.DataFrame(list(zip(X_test, y_test, y_pred_class)),
              columns=['abstract','expected', 'predicted'])
