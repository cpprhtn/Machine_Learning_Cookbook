#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 22:59:18 2020

@author: cpprhtn
"""



import pandas as pd

url = 'https://tinyurl.com/simulated-excel'

dataframe = pd.read_json(url, orient='columns')

dataframe.head(2)