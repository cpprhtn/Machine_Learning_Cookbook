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