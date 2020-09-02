#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 20:39:52 2020

@author: cpprhtn
"""



from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston

boston = load_boston()
features = boston.data[:,0:2]
target = boston.target

regression = LinearRegression()

model = regression.fit(features, target)

#편향
model.intercept_

LinearRegression().fit(features, target).predict(features)[0]*1000