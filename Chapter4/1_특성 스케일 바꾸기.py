#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 20:18:56 2020

@author: cpprhtn
"""



import numpy as np
from sklearn import preprocessing

#특성
feature = np.array([[-500.5],
                    [-100.1],
                    [0],
                    [100.1],
                    [900.9]])

#스케일러 객체
minmax_scale = preprocessing.MinMaxScaler(feature_range=(0, 1))

#특성의 스케일을 변환
scaled_feature = minmax_scale.fit_transform(feature)

scaled_feature

#훈련 세트 변환
preprocessing.MinMaxScaler().fit_transform(feature[:3])

#테스트 세트를 변환
preprocessing.MinMaxScaler().fit_transform(feature[3:])

#훈련 세트로 변환기를 학습
scaler = preprocessing.MinMaxScaler().fit(feature[:3])
scaler.transform(feature[:3])

#훈련 세트에서 학습한 변환기로 테스트 세트를 변환
scaler.transform(feature[3:])