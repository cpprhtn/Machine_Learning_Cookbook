#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 21:54:48 2020

@author: cpprhtn
"""



import numpy as np
from sklearn.metrics import silhouette_score
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

features, _ = make_blobs(n_samples = 1000,
                         n_features = 10,
                         centers = 2,
                         cluster_std = 0.5,
                         shuffle = True,
                         random_state = 1)

model = KMeans(n_clusters=2, random_state=1).fit(features)

#예측된 클래스
target_predicted = model.labels_

silhouette_score(features, target_predicted)