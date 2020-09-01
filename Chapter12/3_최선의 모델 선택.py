#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 20:42:19 2020

@author: cpprhtn
"""



import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline

np.random.seed(0)

iris = datasets.load_iris()
features = iris.data
target = iris.target

#파이프라인
pipe = Pipeline([("classifier", RandomForestClassifier())])

search_space = [{"classifier": [LogisticRegression()],
                 "classifier__penalty": ['l1', 'l2'],
                 "classifier__C": np.logspace(0, 4, 10)},
                {"classifier": [RandomForestClassifier()],
                 "classifier__n_estimators": [10, 100, 1000],
                 "classifier__max_features": [1, 2, 3]}]

gridsearch = GridSearchCV(pipe, search_space, cv=5, verbose=0)

best_model = gridsearch.fit(features, target)

#최선의 모델
best_model.best_estimator_.get_params()["classifier"]

