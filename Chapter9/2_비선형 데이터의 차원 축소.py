#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 17:37:22 2020

@author: cpprhtn
"""



from sklearn.decomposition import KernelPCA
from sklearn.datasets import make_circles

#비선형 데이터
features, _ = make_circles(n_samples=1000, random_state=1, noise=0.1, factor=0.1)

#방사 기저 함수(radius basis function, RBF)를 사용하여 커널 PCA를 적용
kpca = KernelPCA(kernel="rbf", gamma=15, n_components=1)
features_kpca = kpca.fit_transform(features)

print("원본 특성 개수:", features.shape[1])
print("줄어든 특성 개수:", features_kpca.shape[1])

kpca.components_