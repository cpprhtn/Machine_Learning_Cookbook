#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 20:37:52 2020

@author: cpprhtn
"""



import numpy as np
from sklearn import preprocessing

x = np.array([[-1000.1],
              [-200.2],
              [500.5],
              [600.6],
              [9000.9]])

#변환기 객체
scaler = preprocessing.StandardScaler()

#특성 변환
standardized = scaler.fit_transform(x)

standardized

#평균과 표준 편차
print("평균 Mean:", round(standardized.mean()))
print("표준 편차 Standard deviation:", standardized.std())

#변환기 객체
robust_scaler = preprocessing.RobustScaler()

#특성 변환
robust_scaler.fit_transform(x)

interquatile_range = x[3] - x[1]
(x - np.median(x)) / interquatile_range

preprocessing.QuantileTransformer().fit_transform(x)