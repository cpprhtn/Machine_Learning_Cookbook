#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 20:26:24 2020

@author: cpprhtn
"""



import pandas as pd

url = 'https://tinyurl.com/titanic-csv'

dataframe = pd.read_csv(url)

#‘sex’ 열이 ‘female’인 행 중 처음 두 개를 출력
dataframe[dataframe['Sex'] == 'female'].head(2)

#행 필터링
dataframe[(dataframe['Sex'] == 'female') & (dataframe['Age'] >= 65)]

