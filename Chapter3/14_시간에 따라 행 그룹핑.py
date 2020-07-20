#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 22:06:58 2020

@author: cpprhtn
"""



import pandas as pd
import numpy as np

#날짜 범위 만듦
time_index = pd.date_range('06/06/2017', periods=100000, freq='30S')

dataframe = pd.DataFrame(index=time_index)

#난수 값으로 열 만듦
dataframe['Sale_Amount'] = np.random.randint(1, 10, 100000)

#주 단위로 행을 그룹핑한 다음 합을 계산
dataframe.resample('W').sum()

dataframe.head(3)

#2주 단위로 그룹핑하고 평균을 계산
dataframe.resample('2W').mean()

#한 달 간격으로 그룹핑하고 행을 카운트
dataframe.resample('M').count()

#월 간격으로 그룹핑하고 행을 카운트
dataframe.resample('M', label='left').count()

#월 첫째날을 기준으로 변경
dataframe.resample('MS').count()