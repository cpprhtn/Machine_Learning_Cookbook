#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 20:01:41 2020

@author: cpprhtn
"""



from sklearn.datasets import load_boston
from sklearn.dummy import DummyRegressor
from sklearn.model_selection import train_test_split

boston = load_boston()

features, target = boston.data, boston.target

features_train, features_test, target_train, target_test = train_test_split(
    features, target, random_state=0)

#더미 회귀 모델
dummy = DummyRegressor(strategy='mean')

dummy.fit(features_train, target_train)

#R^2 점수
dummy.score(features_test, target_test)




from sklearn.linear_model import LinearRegression

#간단한 선형 회귀 모델
ols = LinearRegression()
ols.fit(features_train, target_train)

#R^2 점수
ols.score(features_test, target_test)


#20으로 예측하는 더미 회귀 모델
clf = DummyRegressor(strategy='constant', constant=20)
clf.fit(features_train, target_train)

#점수
clf.score(features_test, target_test)


clf = DummyRegressor(strategy='quantile', quantile=1.0)
clf.fit(features_train, target_train)

#훈련 세트 타깃의 최대값으로 예측
clf.predict(features_test)

import numpy as np
#훈련 세트의 타깃에서 최댓값
np.max(target_train)