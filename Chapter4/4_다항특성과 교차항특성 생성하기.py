#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 21:05:13 2020

@author: cpprhtn
"""



import numpy as np
from sklearn.preprocessing import PolynomialFeatures

features = np.array([[2, 3],
                     [2, 3],
                     [2, 3]])

#PolynomialFeatures 객체
polynomial_interaction = PolynomialFeatures(degree=2, include_bias=False)

#다항 특성
polynomial_interaction.fit_transform(features)

interaction = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)
interaction.fit_transform(features)

#상수항 1을 추가
polynomial_bias = PolynomialFeatures(degree=2, include_bias=True).fit(features)
polynomial_bias.transform(features)

polynomial_bias.get_feature_names()