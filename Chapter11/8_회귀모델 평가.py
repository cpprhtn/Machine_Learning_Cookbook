#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 21:45:43 2020

@author: cpprhtn
"""



from sklearn.datasets import make_regression
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

features, target = make_regression(n_samples = 100,
                                   n_features = 3,
                                   n_informative = 3,
                                   n_targets = 1,
                                   noise = 50,
                                   coef = False,
                                   random_state = 1)

#선형 회귀 모델
ols = LinearRegression()

#음의 MSE를 사용한 교차검증
cross_val_score(ols, features, target, scoring='neg_mean_squared_error')

#R^2를 사용한 교차검증
cross_val_score(ols, features, target, scoring='r2')