# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 19:55:50 2018

@author: ham2026
"""

from urllib import request 
from bs4 import BeautifulSoup
from nltk import word_tokenize

#def Get_the_page_by_beautifulsoup(webpage):  **this is what the function is called in your textbook
def text_from_webpage(webpage):
    #open the webpage and read it 
    html = request.urlopen(webpage).read().decode('utf-8')
    # convert the text from html to plain text 
    raw = BeautifulSoup(html, 'html.parser').get_text()
    #tokenize each word 
    tokens = word_tokenize(raw)
    #text = nltk.Text(tokens)
    return tokens  

#Wikipedia works
webpagetoken = text_from_webpage("https://en.wikipedia.org/wiki/Natural_language_processing")

def webpage_to_txt(webpage, fileName): 
    print("working")
    #path = 'C:/Users/ham2026/Documents/Python/WCM-Course/'
    html = request.urlopen(webpage).read().decode('utf8')
    raw = BeautifulSoup(html, 'html.parser').get_text()
    f = open(str(fileName), 'w')
    f.write(str(raw))
    f.close()
    print("done")
    
print("hi")
webpage_to_txt("https://en.wikipedia.org/wiki/Natural_language_processing", "NLPwiki.txt")