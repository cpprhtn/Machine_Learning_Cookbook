#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 21:33:24 2020

@author: cpprhtn
"""



import pandas as pd

dataframe = pd.DataFrame()

dataframe['date'] = pd.date_range('1/1/2001', periods=100000, freq='H')

dataframe[(dataframe['date'] > '2002-1-1 01:00:00') &
          (dataframe['date'] <= '2002-1-1 04:00:00')]

# 인덱스 설정
dataframe = dataframe.set_index(dataframe['date'])

dataframe.loc['2002-1-1 01:00:00':'2002-1-1 04:00:00']

