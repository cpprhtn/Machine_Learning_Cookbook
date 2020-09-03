#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 19:58:03 2020

@author: cpprhtn
"""



from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets

iris = datasets.load_iris()
features = iris.data
target = iris.target

randomforest = RandomForestClassifier(random_state=0, n_jobs=-1)

model = randomforest.fit(features, target)

observation = [[ 5,  4,  3,  2]]
.
model.predict(observation)

randomforest_entropy = RandomForestClassifier(
    criterion="entropy", random_state=0)

model_entropy = randomforest_entropy.fit(features, target)