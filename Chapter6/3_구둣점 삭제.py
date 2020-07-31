#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 20:43:55 2020

@author: cpprhtn
"""



import unicodedata
import sys

text_data = ['Hi!!!! I. Love. This. Song....',
             '10000% Agree!!!! #LoveIT',
             'Right?!?!']

#구두점 문자로 이루어진 딕셔너리
punctuation = dict.fromkeys(i for i in range(sys.maxunicode)
                            if unicodedata.category(chr(i)).startswith('P'))

#문자열의 구두점을 삭제
[string.translate(punctuation) for string in text_data]