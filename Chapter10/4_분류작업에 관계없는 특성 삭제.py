#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 16:42:58 2020

@author: cpprhtn
"""



from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2, f_classif

iris = load_iris()
features = iris.data
target = iris.target

#범주형 데이터를 정수형으로 변환
features = features.astype(int)

#카이제곱 통계값이 가장 큰 특성 두 개를 선택
chi2_selector = SelectKBest(chi2, k=2)
features_kbest = chi2_selector.fit_transform(features, target)

print("원본 특성 개수:", features.shape[1])
print("줄어든 특성 개수:", features_kbest.shape[1])

#F-값이 가장 높은 특성 두 개를 선택
fvalue_selector = SelectKBest(f_classif, k=2)
features_kbest = fvalue_selector.fit_transform(features, target)

print("원본 특성 개수:", features.shape[1])
print("줄어든 특성 개수:", features_kbest.shape[1])

from sklearn.feature_selection import SelectPercentile

#가장 큰 F-값의 상위 75% 특성을 선택
fvalue_selector = SelectPercentile(f_classif, percentile=75)
features_kbest = fvalue_selector.fit_transform(features, target)

print("원본 특성 개수:", features.shape[1])
print("줄어든 특성 개수:", features_kbest.shape[1])

