#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 20:06:17 2020

@author: cpprhtn
"""



import pandas as pd

url = 'https://tinyurl.com/titanic-csv'

dataframe = pd.read_csv(url)

#첫 번째 행
dataframe.iloc[0]

#세 개의 행
dataframe.iloc[1:4]

#네 개의 행
dataframe.iloc[:4]

#인덱스 설정
dataframe = dataframe.set_index(dataframe['Name'])

#행 확인
dataframe.loc['Allen, Miss Elisabeth Walton']

#'Allison, Miss Helen Loraine' 이전까지 Age 열과 Sex 열만 선택
dataframe.loc[:'Allison, Miss Helen Loraine', 'Age':'Sex']

#dataframe[:2]와 동일
dataframe[:'Allison, Miss Helen Loraine']