#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 22:45:41 2020

@author: cpprhtn
"""



import pandas as pd

url = 'https://tinyurl.com/titanic-csv'

dataframe = pd.read_csv(url)

#통곗값 계산
print('최댓값:', dataframe['Age'].max())
print('최솟값:', dataframe['Age'].min())
print('평균:', dataframe['Age'].mean())
print('합:', dataframe['Age'].sum())
print('카운트:', dataframe['Age'].count())

#카운트 출력
dataframe.count()

#수치형 열의 공분산 계산
dataframe.cov()


#수치형 열의 상관계수 계산
dataframe.corr()

