# -*- coding: utf-8 -*-
import pandas as pd 
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords 

df = pd.read_csv('../noteevents_top10.csv', nrows = 5)
dfDischarge = df.loc[df['CATEGORY']== 'Discharge summary'] 
notesList = dfDischarge["TEXT"].tolist()

# write to csv
dfDischarge.to_csv('first5.csv')
# write to text file
f = open('first5.txt', 'w')
for pt_note in notesList: 
    f.write("-"*80)
    f.write(pt_note)
f.close()
