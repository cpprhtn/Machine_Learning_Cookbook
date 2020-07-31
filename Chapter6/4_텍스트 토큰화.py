#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 21:05:29 2020

@author: cpprhtn
"""



import nltk
nltk.download('punkt')

from nltk.tokenize import word_tokenize

string = "The science of today is the technology of tomorrow"

#단어를 토큰으로 나누기
word_tokenize(string)

from nltk.tokenize import sent_tokenize

string = "The science of today is the technology of tomorrow. Tomorrow is today."

#문장으로 나누기
sent_tokenize(string)