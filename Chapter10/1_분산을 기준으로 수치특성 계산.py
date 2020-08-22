#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 15:55:17 2020

@author: cpprhtn
"""




from sklearn import datasets
from sklearn.feature_selection import VarianceThreshold


iris = datasets.load_iris()


features = iris.data
target = iris.target

#기준값
thresholder = VarianceThreshold(threshold=.5)

#기준값보다 높은 특성을 선택
features_high_variance = thresholder.fit_transform(features)

features_high_variance[0:3]

#분산을 확인
thresholder.variances_

from sklearn.preprocessing import StandardScaler

#표준화
scaler = StandardScaler()
features_std = scaler.fit_transform(features)

#각 특성의 분산
selector = VarianceThreshold()
selector.fit(features_std).variances_