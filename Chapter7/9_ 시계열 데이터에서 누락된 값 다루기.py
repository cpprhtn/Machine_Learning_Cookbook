#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 22:57:02 2020

@author: cpprhtn
"""



import pandas as pd
import numpy as np

time_index = pd.date_range("01/01/2010", periods=5, freq="M")

dataframe = pd.DataFrame(index=time_index)

#누락된 값이 있는 특성을 만들기
dataframe["Sales"] = [1.0,2.0,np.nan,np.nan,5.0]

#누락된 값을 보간
dataframe.interpolate()

#앞쪽으로 채우기(Forward-fill)
dataframe.ffill()

#뒤쪽으로 채우기(Back-fill)
dataframe.bfill()

#누락된 값 보간하기
dataframe.interpolate(method="quadratic")

#누락된 값 보간하기
dataframe.interpolate(limit=1, limit_direction="forward")