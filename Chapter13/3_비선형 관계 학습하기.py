#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 21:19:22 2020

@author: cpprhtn
"""



from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
from sklearn.preprocessing import PolynomialFeatures

boston = load_boston()
features = boston.data[:,0:1]
target = boston.target

#다항 특성 x^2와 x^3
polynomial = PolynomialFeatures(degree=3, include_bias=False)
features_polynomial = polynomial.fit_transform(features)

regression = LinearRegression()

model = regression.fit(features_polynomial, target)

#첫 번째 샘플을 x^2로 거듭제곱
features[0]**2

#첫 번째 샘플을 x^2로 세제곱
features[0]**3

features_polynomial[0]