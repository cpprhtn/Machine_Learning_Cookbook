#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 21:20:22 2020

@author: cpprhtn
"""



import numpy as np
from sklearn import linear_model, datasets
from sklearn.model_selection import GridSearchCV

iris = datasets.load_iris()
features = iris.data
target = iris.target

logistic = linear_model.LogisticRegression()

#규제 페널티의 후보
penalty = ["l1", "l2"]

#C 값의 후보 범위
C = np.logspace(0, 4, 1000)

#하이퍼파라미터
hyperparameters = dict(C=C, penalty=penalty)

gridsearch = GridSearchCV(logistic, hyperparameters, cv=5, n_jobs=-1, verbose=1)

best_model = gridsearch.fit(features, target)

#하나의 코어만 사용하는 그리드 서치 객체
clf = GridSearchCV(logistic, hyperparameters, cv=5, n_jobs=1, verbose=1)

best_model = clf.fit(features, target)

