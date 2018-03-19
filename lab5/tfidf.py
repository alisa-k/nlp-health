# -*- coding: utf-8 -*-
# https://cran.r-project.org/web/packages/tidytext/vignettes/tf_idf.html
from sklearn.feature_extraction.text import TfidfVectorizer
# these are 2 different documents
corpus = ["This is very strange",
          "This is very nice"]
vectorizer = TfidfVectorizer(min_df=1)
X = vectorizer.fit_transform(corpus)
idf = vectorizer.idf_
print(dict(zip(vectorizer.get_feature_names(), idf)))