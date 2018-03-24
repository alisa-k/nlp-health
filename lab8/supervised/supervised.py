import pandas as pd
from sklearn import datasets, linear_model
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

# get the data, divide it into training and testing data sets
df = pd.read_csv('data/binary_classification_data.csv')
df['label_num'] = df.label.map({'ankle':0, 'head':1})

X = df.abstract
y = df.label_num

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)

#learn training data vocabulary, then use it to create a document-term matrix
vect = CountVectorizer()
X_train_dtm = vect.fit_transform(X_train)
X_test_dtm = vect.transform(X_test)

# fit a model
lm = linear_model.LinearRegression()
model = lm.fit(X_train_dtm, y_train)
predictions = lm.predict(X_test_dtm)
df2 = pd.DataFrame(X_test)
df2['actual'] = y_test
df2['predicted'] = predictions
print("Score:", model.score(X_test_dtm, y_test))

# print plot 

##### BINARY CLASSIFIER #####
from sklearn import tree
from sklearn import metrics

clf = tree.DecisionTreeClassifier(criterion='entropy')
# train the model using X_train_dtm (timing it with an IPython "magic command")
%time clf.fit(X_train_dtm, y_train)
# make class predictions for X_test_dtm
y_pred_class = clf.predict(X_test_dtm)
# calculate accuracy of class predictions
metrics.accuracy_score(y_test, y_pred_class)
# print message text for the false positives (ham incorrectly classified as spam)
X_test[y_test < y_pred_class]
df2 = pd.DataFrame(X_test)
df2['actual'] = y_test
df2['predicted'] = y_pred_class