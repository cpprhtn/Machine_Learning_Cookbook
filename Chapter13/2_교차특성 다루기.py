#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 21:04:53 2020

@author: cpprhtn
"""



from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
from sklearn.preprocessing import PolynomialFeatures

boston = load_boston()
features = boston.data[:,0:2]
target = boston.target

#교차 항
interaction = PolynomialFeatures(
    degree=3, include_bias=False, interaction_only=True)
features_interaction = interaction.fit_transform(features)

regression = LinearRegression()

model = regression.fit(features_interaction, target)

import numpy as np

#각 샘플에서 첫 번째와 두 번째 특성을 곱함
interaction_term = np.multiply(features[:, 0], features[:, 1])

#첫 번째 샘플의 교차 항
interaction_term[0]

#첫 번째 샘플의 값
features_interaction[0]