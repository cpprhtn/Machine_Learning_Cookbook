#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 21:40:12 2020

@author: cpprhtn
"""



import numpy as np
from sklearn import linear_model, datasets
from sklearn.model_selection import GridSearchCV, cross_val_score

# 데이터를 로드합니다.
iris = datasets.load_iris()
features = iris.data
target = iris.target

# 로지스틱 회귀 모델을 만듭니다.
logistic = linear_model.LogisticRegression(solver='liblinear', multi_class='auto')

# Create range of 20 candidate values for C
C = np.logspace(0, 4, 20)

# 하이퍼파라미터 옵션을 만듭니다.
hyperparameters = dict(C=C)

# 그리드 서치 객체를 만듭니다.
gridsearch = GridSearchCV(logistic, hyperparameters, cv=5, n_jobs=-1, verbose=0, iid=False)

# 중첩 교차검증을 수행하고 평균 점수를 출력합니다.
cross_val_score(gridsearch, features, target, cv=3).mean()

gridsearch = GridSearchCV(logistic, hyperparameters, cv=5, verbose=1, iid=False)
best_model = gridsearch.fit(features, target)
scores = cross_val_score(gridsearch, features, target, cv=3)