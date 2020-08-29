#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 20:17:02 2020

@author: cpprhtn
"""



from sklearn.datasets import load_iris
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import train_test_split

iris = load_iris()

features, target = iris.data, iris.target

features_train, features_test, target_train, target_test = train_test_split(
features, target, random_state=0)

dummy = DummyClassifier(strategy='uniform', random_state=1)

dummy.fit(features_train, target_train)

#정확도
dummy.score(features_test, target_test)


from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier()

classifier.fit(features_train, target_train)

classifier.score(features_test, target_test)
