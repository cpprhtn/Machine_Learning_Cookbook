#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 21:31:56 2020

@author: cpprhtn
"""


import pandas as pd

#데이터 URL
url = 'https://tinyurl.com/simulated-data'


dataframe = pd.read_csv(url)


dataframe.head(2)

#1~10번째 행을 건너 뛰고 한 행 읽음
dataframe = pd.read_csv(url, skiprows=range(1, 11), nrows=1)
dataframe