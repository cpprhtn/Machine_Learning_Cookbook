#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 21:20:09 2020

@author: cpprhtn
"""



import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords

#단어 토큰
tokenized_words = ['i',
                   'am',
                   'going',
                   'to',
                   'go',
                   'to',
                   'the',
                   'store',
                   'and',
                   'park']

#불용어 적재
stop_words = stopwords.words('english')

#불용어 삭제
[word for word in tokenized_words if word not in stop_words]

stop_words[:5]

stopwords.abspath 
#<bound method CorpusReader.abspath of <WordListCorpusReader in '/home/haesun/nltk_data/corpora/stopwords'>>