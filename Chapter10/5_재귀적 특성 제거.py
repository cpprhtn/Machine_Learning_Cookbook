#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 16:55:52 2020

@author: cpprhtn
"""



from sklearn.datasets import make_regression
from sklearn.feature_selection import RFECV
from sklearn import datasets, linear_model

features, target = make_regression(n_samples = 10000,
                                   n_features = 100,
                                   n_informative = 2,
                                   random_state = 1)

#선형 회귀 모델
ols = linear_model.LinearRegression()

#재귀적으로 특성을 제거
rfecv = RFECV(estimator=ols, step=1, scoring="neg_mean_squared_error")
rfecv.fit(features, target)
rfecv.transform(features)

#최선의 특성 개수
rfecv.n_features_

#선택된 특성이 표시된 불리언 마스크
rfecv.support_

#특성의 순위: 최고(1)에서 최악(96)까지
rfecv.ranking_

from sklearn.feature_selection import RFE

rfe = RFE(estimator=ols, n_features_to_select=3)
rfe.fit(features, target)
rfe.transform(features)

np.all(rfe.support_ == rfecv.support_)