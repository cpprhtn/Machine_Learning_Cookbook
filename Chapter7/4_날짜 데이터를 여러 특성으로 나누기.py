#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 21:54:53 2020

@author: cpprhtn
"""



import pandas as pd

dataframe = pd.DataFrame()

dataframe['date'] = pd.date_range('1/1/2001', periods=150, freq='W')

dataframe['year'] = dataframe['date'].dt.year
dataframe['month'] = dataframe['date'].dt.month
dataframe['day'] = dataframe['date'].dt.day
dataframe['hour'] = dataframe['date'].dt.hour
dataframe['minute'] = dataframe['date'].dt.minute

dataframe.head(3)