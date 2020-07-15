#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 17:40:18 2020

@author: cpprhtn
"""



import pandas as pd

url = 'https://tinyurl.com/titanic-csv'

dataframe = pd.read_csv(url)

#mele 행을 삭제
dataframe[dataframe['Sex'] != 'male'].head(2)

dataframe[dataframe['Name'] != 'Allison, Miss Helen Loraine'].head(2)

dataframe[dataframe.index != 0].head(2)