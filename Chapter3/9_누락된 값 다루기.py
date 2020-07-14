#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 00:03:29 2020

@author: cpprhtn
"""



import pandas as pd

url = 'https://tinyurl.com/titanic-csv'

dataframe = pd.read_csv(url)

#누락된 값을 선택하고 두 개의 행을 출력
dataframe[dataframe['Age'].isnull()].head(2)

#NaN으로 값을 바꾸기
#numpy 필요
dataframe['Sex'] = dataframe['Sex'].replace('male', NaN)

import numpy as np

#NaN으로 값 바꾸기
dataframe['Sex'] = dataframe['Sex'].replace('male', np.nan)

#데이터를 적재하고 누란된 값을 설정
dataframe = pd.read_csv(url, na_values=[np.nan, 'NONE', -999])


#'female' 문자열만 NaN으로 인식
dataframe = pd.read_csv(url, na_values=['female'], 
                        keep_default_na=False)
dataframe[12:14]


#na_filter를 False로 설정하면 NaN변환을 하지 않음
dataframe = pd.read_csv(url, na_filter=False)
dataframe[12:14]