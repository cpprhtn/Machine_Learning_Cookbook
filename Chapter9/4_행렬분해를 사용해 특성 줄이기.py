#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 18:13:42 2020

@author: cpprhtn
"""



from sklearn.decomposition import NMF
from sklearn import datasets

digits = datasets.load_digits()

features = digits.data

#NMF 적용
nmf = NMF(n_components=10, random_state=1)
features_nmf = nmf.fit_transform(features)

print("원본 특성 개수:", features.shape[1])
print("줄어든 특성 개수:", features_nmf.shape[1])

nmf.components_.shape

np.all(nmf.components_ >= 0)

np.mean(features - np.dot(features_nmf, nmf.components_))

nmf_mu = NMF(n_components=10, solver='mu', random_state=1)
features_nmf_mu = nmf_mu.fit_transform(features)

np.mean(features - np.dot(features_nmf_mu, nmf_mu.components_))