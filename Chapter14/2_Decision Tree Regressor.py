#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 19:32:34 2020

@author: cpprhtn
"""



from sklearn.tree import DecisionTreeRegressor
from sklearn import datasets

boston = datasets.load_boston()
features = boston.data[:,0:2]
target = boston.target

decisiontree = DecisionTreeRegressor(random_state=0)

model = decisiontree.fit(features, target)

observation = [[0.02, 16]]

model.predict(observation)

#평균 제곱 오차를 사용
decisiontree_mae = DecisionTreeRegressor(criterion="mae", random_state=0)

model_mae = decisiontree_mae.fit(features, target)