#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 21:08:38 2020

@author: cpprhtn
"""



import pandas as pd
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

#모의 특성 행렬
features, _ = make_blobs(n_samples = 50,
                         n_features = 2,
                         centers = 3,
                         random_state = 1)

dataframe = pd.DataFrame(features, columns=["feature_1", "feature_2"])

#k-평균 군집 모델
clusterer = KMeans(3, random_state=0)

#모델 훈련
clusterer.fit(features)

#그룹 소속 예측
dataframe["group"] = clusterer.predict(features)

dataframe.head(5)