#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 20:56:01 2020

@author: cpprhtn
"""



import pandas as pd

url = 'https://tinyurl.com/titanic-csv'

dataframe = pd.read_csv(url)

#행을 그룹핑한 다음 함수를 적용
dataframe.groupby('Sex').apply(lambda x: x.count())
