#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 21:06:38 2020

@author: cpprhtn
"""



import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

np.random.seed(0)

iris = datasets.load_iris()
features = iris.data
target = iris.target

#StandardScaler와 PCA를 포함한 전처리 객체
preprocess = FeatureUnion([("std", StandardScaler()), ("pca", PCA())])

#파이프라인
pipe = Pipeline([("preprocess", preprocess),
                 ("classifier", LogisticRegression())])

#후보 값 정의
search_space = [{"preprocess__pca__n_components": [1, 2, 3],
                 "classifier__penalty": ["l1", "l2"],
                 "classifier__C": np.logspace(0, 4, 10)}]

clf = GridSearchCV(pipe, search_space, cv=5, verbose=0, n_jobs=-1)

best_model = clf.fit(features, target)