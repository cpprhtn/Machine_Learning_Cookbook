#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 22:56:23 2020

@author: cpprhtn
"""



import pandas as pd

dataframe = pd.DataFrame()

dataframe['Arrived'] = [pd.Timestamp('01-01-2017'), pd.Timestamp('01-04-2017')]
dataframe['Left'] = [pd.Timestamp('01-01-2017'), pd.Timestamp('01-06-2017')]

dataframe['Left'] - dataframe['Arrived']

#특성 간의 기간을 계산
pd.Series(delta.days for delta in (dataframe['Left'] - dataframe['Arrived']))