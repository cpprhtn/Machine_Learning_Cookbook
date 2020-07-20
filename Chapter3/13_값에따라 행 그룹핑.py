#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 21:41:43 2020

@author: cpprhtn
"""



import pandas as pd

url = 'https://tinyurl.com/titanic-csv'

dataframe = pd.read_csv(url)

#‘Sex’ 열의 값으로 행 그룹핑, 평균 계산
dataframe.groupby('Sex').mean()

#행 그룹핑
dataframe.groupby('Sex')

dataframe.groupby('Survived')['Name'].count()

dataframe.groupby(['Sex','Survived'])['Age'].mean()