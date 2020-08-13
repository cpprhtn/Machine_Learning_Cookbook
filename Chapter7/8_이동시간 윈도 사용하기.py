#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 22:27:48 2020

@author: cpprhtn
"""



import pandas as pd

time_index = pd.date_range("01/01/2010", periods=5, freq="M")

dataframe = pd.DataFrame(index=time_index)

dataframe["Stock_Price"] = [1,2,3,4,5]

dataframe.rolling(window=2).mean()

dataframe.ewm(alpha=0.5).mean()