#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 22:07:50 2020

@author: cpprhtn
"""



import numpy as np
from fancyimpute import KNN
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_blobs

#모의 특성 행렬
features, _ = make_blobs(n_samples = 1000,
                         n_features = 2,
                         random_state = 1)

#특성 표준화
scaler = StandardScaler()
standardized_features = scaler.fit_transform(features)

#첫 번째 샘플의 첫 번째 특성을 삭제
true_value = standardized_features[0,0]
standardized_features[0,0] = np.nan

#특성 행렬에 있는 누락된 값을 예측
features_knn_imputed = KNN(k=5, verbose=0).fit_transform(standardized_features)

#실제 값과 대체된 값을 비교
print("실제 값:", true_value)
print("대체된 값:", features_knn_imputed[0,0])

from sklearn.impute import SimpleImputer

simple_imputer = SimpleImputer()
features_simple_imputed = simple_imputer.fit_transform(features)

#실제 값과 대체된 값을 비교
print("실제 값 True Value:", true_value)
print("대체된 값 Imputed Value:", features_simple_imputed[0,0])