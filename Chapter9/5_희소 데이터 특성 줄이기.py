#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 18:24:04 2020

@author: cpprhtn
"""



from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import TruncatedSVD
from scipy.sparse import csr_matrix
from sklearn import datasets
import numpy as np

digits = datasets.load_digits()

features = StandardScaler().fit_transform(digits.data)

features_sparse = csr_matrix(features)

#TSVD 객체
tsvd = TruncatedSVD(n_components=10)

features_sparse_tsvd = tsvd.fit(features_sparse).transform(features_sparse)

print("원본 특성 개수:", features_sparse.shape[1])
print("줄어든 특성 개수:", features_sparse_tsvd.shape[1])

#처음 세 개의 성분이 설명하는 분산의 비율 합
tsvd.explained_variance_ratio_[0:3].sum()

#특성 개수보다 하나 작은 TSVD
tsvd = TruncatedSVD(n_components=features_sparse.shape[1]-1)
features_tsvd = tsvd.fit(features)

tsvd_var_ratios = tsvd.explained_variance_ratio_

def select_n_components(var_ratio, goal_var):
    total_variance = 0.0

    n_components = 0

    for explained_variance in var_ratio:

        total_variance += explained_variance

        n_components += 1

        if total_variance >= goal_var:
            break

    return n_components

select_n_components(tsvd_var_ratios, 0.95) #Out[]: 40

features = digits.data - np.mean(digits.data, axis=0)

pca = PCA(n_components=40, random_state=1)
features_pca = pca.fit_transform(features)

tsvd = TruncatedSVD(n_components=40, random_state=1)
features_tsvd = tsvd.fit_transform(features)

np.max(np.abs(features_pca - features_tsvd))