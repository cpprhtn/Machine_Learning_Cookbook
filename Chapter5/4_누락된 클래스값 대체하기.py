#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 22:45:14 2020

@author: cpprhtn
"""



import numpy as np
from sklearn.neighbors import KNeighborsClassifier

X = np.array([[0, 2.10, 1.45],
              [1, 1.18, 1.33],
              [0, 1.22, 1.27],
              [1, -0.21, -1.19]])

#누락된 값이 있는 특성 행렬을 만들기
X_with_nan = np.array([[np.nan, 0.87, 1.31],
                       [np.nan, -0.67, -0.22]])

#KNN 학습기를 훈련
clf = KNeighborsClassifier(3, weights='distance')
trained_model = clf.fit(X[:,1:], X[:,0])

#누락된 값의 클래스를 예측
imputed_values = trained_model.predict(X_with_nan[:,1:])

#예측된 클래스와 원본 특성을 열로 합침
X_with_imputed = np.hstack((imputed_values.reshape(-1,1), X_with_nan[:,1:]))

#두 특성 행렬을 연결
np.vstack((X_with_imputed, X))

from sklearn.impute import SimpleImputer

#두 개의 특성 행렬 합치기
X_complete = np.vstack((X_with_nan, X))

imputer = SimpleImputer(strategy='most_frequent')
imputer.fit_transform(X_complete)