# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 17:20:51 2018

@author: ham2026
"""


import pandas as pd 
import nltk 

df = pd.read_csv('NOTEEVENTS.csv', nrows = 5)
print(df)

print(len(df.columns))

print(df.columns[10])

print(df["TEXT"])


print(df["TEXT"][0])

notes = df["TEXT"]
print(type(notes))

txt = str(notes)

df['tokenized_text'] = df['TEXT'].apply(nltk.word_tokenize) 

tokenizedTextList = df['tokenized_text'].tolist()
print(tokenizedTextList)


notesText = nltk.Text(notes)
print(notesText)
print(type(notesText))

notesText.collocations()

def csv_tokenizedTextList(num_of_rows): 
    df = pd.read_csv('noteevents_top10.csv', nrows = num_of_rows)
    df['tokenized_text'] = df['TEXT'].apply(nltk.word_tokenize) 
    tokenizedTextList = df['tokenized_text'].tolist()
    return tokenizedTextList 



