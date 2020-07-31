#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 21:46:04 2020

@author: cpprhtn
"""



from nltk.stem.porter import PorterStemmer

#단어 토큰
tokenized_words = ['i', 'am', 'humbled', 'by', 'this', 'traditional', 'meeting']

#어간 추출기
porter = PorterStemmer()

#어간 추출기 적용
[porter.stem(word) for word in tokenized_words]