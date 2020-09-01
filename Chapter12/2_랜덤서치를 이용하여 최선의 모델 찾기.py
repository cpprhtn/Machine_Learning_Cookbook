#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 20:19:52 2020

@author: cpprhtn
"""



from scipy.stats import uniform
from sklearn import linear_model, datasets
from sklearn.model_selection import RandomizedSearchCV

iris = datasets.load_iris()
features = iris.data
target = iris.target

logistic = linear_model.LogisticRegression()

penalty = ['l1', 'l2']

#규제 하이퍼파라미터 값의 분포
C = uniform(loc=0, scale=4)

#하이퍼파라미터 옵션
hyperparameters = dict(C=C, penalty=penalty)

#랜덤 서치 객체
randomizedsearch = RandomizedSearchCV(
    logistic, hyperparameters, random_state=1, n_iter=100, cv=5, verbose=0,
    n_jobs=-1)

#랜덤 서치 수행
best_model = randomizedsearch.fit(features, target)

print('가장 좋은 페널티:', best_model.best_estimator_.get_params()['penalty'])
print('가장 좋은 C 값:', best_model.best_estimator_.get_params()['C'])