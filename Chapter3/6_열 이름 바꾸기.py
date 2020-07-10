#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 22:34:13 2020

@author: cpprhtn
"""



import pandas as pd

url = 'https://tinyurl.com/titanic-csv'

dataframe = pd.read_csv(url)

#열 이름을 바꾸기
dataframe.rename(columns={'PClass': 'Passenger Class'}).head(2)


import collections
#딕셔너리
column_names = collections.defaultdict(str)

#키
for name in dataframe.columns:
    column_names[name]

#딕셔너리 출력
column_names

#인덱스 0을 -1로 바꾸
dataframe.rename(index={0:-1}).head(2)

#열 이름을 소문자로 바꾸
dataframe.rename(str.lower, axis='columns').head(2)