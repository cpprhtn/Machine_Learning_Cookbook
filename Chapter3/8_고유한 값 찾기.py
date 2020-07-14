#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 22:57:07 2020

@author: cpprhtn
"""



import pandas as pd

url = 'https://tinyurl.com/titanic-csv'

dataframe = pd.read_csv(url)

dataframe['Sex'].unique()

#카운트 출력
dataframe['Sex'].value_counts()

dataframe['PClass'].value_counts()

#고유한 값의 개수 출력
dataframe['PClass'].nunique()

#nunique 메서드는 데이터프레임 전체에 적용가능
dataframe.nunique()

