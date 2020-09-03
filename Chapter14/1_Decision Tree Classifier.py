#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 19:17:14 2020

@author: cpprhtn
"""



from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets

iris = datasets.load_iris()
features = iris.data
target = iris.target

decisiontree = DecisionTreeClassifier(random_state=0)

model = decisiontree.fit(features, target)

observation = [[ 5,  4,  3,  2]]

model.predict(observation)

model.predict_proba(observation)

#엔트로피
decisiontree_entropy = DecisionTreeClassifier(
    criterion='entropy', random_state=0)

model_entropy = decisiontree_entropy.fit(features, target)