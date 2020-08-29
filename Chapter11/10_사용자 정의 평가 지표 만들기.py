#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 22:08:50 2020

@author: cpprhtn
"""



from sklearn.metrics import make_scorer, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.datasets import make_regression

features, target = make_regression(n_samples = 100,
                                   n_features = 3,
                                   random_state = 1)

features_train, features_test, target_train, target_test = train_test_split(
     features, target, test_size=0.10, random_state=1)

#사용자 정의 지표
def custom_metric(target_test, target_predicted):
    #R^2 점수
    r2 = r2_score(target_test, target_predicted)
    return r2

score = make_scorer(custom_metric, greater_is_better=True)

#릿지(ridge) 회귀 모델
classifier = Ridge()

model = classifier.fit(features_train, target_train)

#사용자 정의 스코어 함수 적용
score(model, features_test, target_test)

#예측
target_predicted = model.predict(features_test)

#R^2 점수
r2_score(target_test, target_predicted)