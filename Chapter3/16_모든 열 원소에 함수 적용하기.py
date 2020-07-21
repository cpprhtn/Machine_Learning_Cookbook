#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 20:36:55 2020

@author: cpprhtn
"""



import pandas as pd

url = 'https://tinyurl.com/titanic-csv'

dataframe = pd.read_csv(url)

def uppercase(x):
    return x.upper()

#함수 적용
dataframe['Name'].apply(uppercase)[0:2]

#Survived 열의 1을 Live로, 0을 Dead로 바꿈
dataframe['Survived'].map({1:'Live', 0:'Dead'})[:5]

#함수의 매개변수(age)를 apply 메서드를 호출할 때 전달가능
dataframe['Age'].apply(lambda x, age: x < age, age=30)[:5]

#각 열에서 가장 큰 값 찾기
dataframe.apply(lambda x: max(x))


def truncate_string(x):
    if type(x) == str:
        return x[:20]
    return x

#문자열의 길이를 최대 20자로 줄이기
dataframe.applymap(truncate_string)[:5]