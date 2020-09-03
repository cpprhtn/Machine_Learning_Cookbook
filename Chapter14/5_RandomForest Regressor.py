#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 20:14:32 2020

@author: cpprhtn
"""



from sklearn.ensemble import RandomForestRegressor
from sklearn import datasets

boston = datasets.load_boston()
features = boston.data[:,0:2]
target = boston.target

randomforest = RandomForestRegressor(random_state=0, n_jobs=-1)

model = randomforest.fit(features, target)