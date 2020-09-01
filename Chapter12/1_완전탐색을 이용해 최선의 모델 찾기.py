#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 19:48:45 2020

@author: cpprhtn
"""



import numpy as np
from sklearn import linear_model, datasets
from sklearn.model_selection import GridSearchCV

iris = datasets.load_iris()
features = iris.data
target = iris.target

#로지스틱 회귀
logistic = linear_model.LogisticRegression()

#페널티(penalty) 하이퍼파라미터 값
penalty = ['l1', 'l2']

#규제 하이퍼파라미터 값의 범위
C = np.logspace(0, 4, 10)

#하이퍼파라미터 후보 딕셔너리
hyperparameters = dict(C=C, penalty=penalty)

#그리드 서치 객체
gridsearch = GridSearchCV(logistic, hyperparameters, cv=5, verbose=0)

#그리드 서치
best_model = gridsearch.fit(features, target)

#최선의 하이퍼파라미터
print('가장 좋은 페널티:', best_model.best_estimator_.get_params()['penalty'])
print('가장 좋은 C 값:', best_model.best_estimator_.get_params()['C'])
