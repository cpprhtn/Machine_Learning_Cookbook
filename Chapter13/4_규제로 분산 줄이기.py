#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 21:38:38 2020

@author: cpprhtn
"""



from sklearn.linear_model import Ridge
from sklearn.datasets import load_boston
from sklearn.preprocessing import StandardScaler

boston = load_boston()
features = boston.data
target = boston.target

scaler = StandardScaler()
features_standardized = scaler.fit_transform(features)

#alpha 값을 지정한 릿지 회귀
regression = Ridge(alpha=0.5)

model = regression.fit(features_standardized, target)

from sklearn.linear_model import RidgeCV

#세 개의 alpha 값에 대한 릿지 회귀
regr_cv = RidgeCV(alphas=[0.1, 1.0, 10.0])

model_cv = regr_cv.fit(features_standardized, target)

#계수
model_cv.coef_

#5-폴드 교차검증을 사용하여 릿지 회귀 사용
regr_cv = RidgeCV(alphas=[0.1, 1.0, 10.0], cv=5)

model_cv = regr_cv.fit(features_standardized, target)

#alpha 값
model_cv.alpha_