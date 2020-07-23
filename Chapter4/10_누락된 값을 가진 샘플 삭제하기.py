#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 21:40:20 2020

@author: cpprhtn
"""



import numpy as np

features = np.array([[1.1, 11.1],
                     [2.2, 22.2],
                     [3.3, 33.3],
                     [4.4, 44.4],
                     [np.nan, 55]])

#(~ 연산자를 사용하여) 누락된 값이 없는 샘플만 남김
features[~np.isnan(features).any(axis=1)]

import pandas as pd

dataframe = pd.DataFrame(features, columns=["feature_1", "feature_2"])

#누락된 값이 있는 샘플 제거
dataframe.dropna()