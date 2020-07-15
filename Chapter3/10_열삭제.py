#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 17:26:30 2020

@author: cpprhtn
"""



import pandas as pd

url = 'https://tinyurl.com/titanic-csv'

dataframe = pd.read_csv(url)

#열 삭제
dataframe.drop('Age', axis=1).head(2)

dataframe.drop(['Age', 'Sex'], axis=1).head(2)

#PClass 열 삭제
dataframe.drop(dataframe.columns[1], axis=1).head(2)