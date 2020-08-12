#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 23:04:23 2020

@author: cpprhtn
"""



import pandas as pd

dates = pd.Series(pd.date_range("2/2/2002", periods=3, freq="M"))

#요일 확인
dates.dt.day_name()

#요일 확인
dates.dt.weekday