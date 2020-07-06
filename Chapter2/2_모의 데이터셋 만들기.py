#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 21:08:26 2020

@author: cpprhtn
"""



from sklearn.datasets import make_regression

#특성 행렬, 타깃 벡터, 정답 계수를 생성
features, target, coefficients = make_regression(n_samples = 100,
                                                 n_features = 3,
                                                 n_informative = 3,
                                                 n_targets = 1,
                                                 noise = 0.0,
                                                 coef = True,
                                                 random_state = 1)

#특성 행렬과 타깃 벡터를 확인
print('특성 행렬\n', features[:3])
print('타깃 벡터\n', target[:3])


from sklearn.datasets import make_classification

features, target = make_classification(n_samples = 100,
                                       n_features = 3,
                                       n_informative = 3,
                                       n_redundant = 0,
                                       n_classes = 2,
                                       weights = [.25, .75],
                                       random_state = 1)

print('특성 행렬\n', features[:3])
print('타깃 벡터\n', target[:3])


from sklearn.datasets import make_blobs

features, target = make_blobs(n_samples = 100,
                              n_features = 2,
                              centers = 3,
                              cluster_std = 0.5,
                              shuffle = True,
                              random_state = 1)

print('특성 행렬\n', features[:3])
print('타깃 벡터\n', target[:3])


import matplotlib.pyplot as plt

#산점도
plt.scatter(features[:,0], features[:,1], c=target)
plt.show()
