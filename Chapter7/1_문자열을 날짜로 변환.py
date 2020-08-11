#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:58:17 2020

@author: cpprhtn
"""



import numpy as np
import pandas as pd

date_strings = np.array(['03-04-2005 11:35 PM',
                         '23-05-2010 12:01 AM',
                         '04-09-2009 09:09 PM'])

#Timestamp 객체로 형변환
[pd.to_datetime(date, format='%d-%m-%Y %I:%M %p') for date in date_strings]

#datetime으로 형변환
[pd.to_datetime(date, format="%d-%m-%Y %I:%M %p", errors="ignore")
for date in date_strings]

pd.to_datetime(date_strings)