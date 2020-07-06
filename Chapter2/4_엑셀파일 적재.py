#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 21:48:00 2020

@author: cpprhtn
"""



import pandas as pd


url = 'https://tinyurl.com/simulated-excel'

dataframe = pd.read_excel(url, sheet_name=0, header=1)

dataframe.head(2)