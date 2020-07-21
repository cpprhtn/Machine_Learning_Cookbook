#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 20:13:13 2020

@author: cpprhtn
"""



import pandas as pd

url = 'https://tinyurl.com/titanic-csv'

dataframe = pd.read_csv(url)

#처음 두 이름을 대문자로 바꾸어 출력
for name in dataframe['Name'][0:2]:
    print(name.upper())
    
#처음 두 이름을 대문자로 바꾸어 출력
[name.upper() for name in dataframe['Name'][0:2]]

