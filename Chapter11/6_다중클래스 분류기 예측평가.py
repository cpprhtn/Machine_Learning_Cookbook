#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 21:11:48 2020

@author: cpprhtn
"""



from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification

features, target = make_classification(n_samples = 10000,
                           n_features = 3,
                           n_informative = 3,
                           n_redundant = 0,
                           n_classes = 3,
                           random_state = 1)

logit = LogisticRegression()

cross_val_score(logit, features, target, scoring='accuracy')

#마크로 평균 F1 점수
cross_val_score(logit, features, target, scoring='f1_macro')