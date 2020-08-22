#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 16:11:12 2020

@author: cpprhtn
"""



from sklearn.feature_selection import VarianceThreshold
'''
예제 특성 행렬
특성 0: 80%가 클래스 0
특성 1: 80%가 클래스 1
특성 2: 60%가 클래스 0, 40%는 클래스 1
'''
features = [[0, 1, 0],
            [0, 1, 1],
            [0, 1, 0],
            [0, 1, 1],
            [1, 0, 0]]

#분산을 기준으로 함
thresholder = VarianceThreshold(threshold=(.75 * (1 - .75)))
thresholder.fit_transform(features)

thresholder.variances_

import numpy as np
np.var(features, axis=0)