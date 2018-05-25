#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 20:34:18 2018

@author: lnovitz
"""
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from nltk.tokenize import sent_tokenize

req = Request('https://www.thediabetescouncil.com/ultimate-guide-to-the-a1c-test-everything-you-need-to-know/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
print(webpage)
soup = BeautifulSoup(html, "html5lib")
text = soup.get_text(strip=True) #strip html tags
tokens = [t for t in text.split()]
clean_tokens = tokens[:]
sr = stopwords.words('english')
for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)
freq = nltk.FreqDist(tokens)
for key,val in freq.items():
    print (str(key) + ':' + str(val))

freq.plot(20, cumulative=False)
#print(text)
#response = urllib.request.urlopen('')
#html = response.read()
#print(html)
