#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 20:06:54 2020

@author: cpprhtn
"""



import numpy as np
from sklearn.covariance import EllipticEnvelope
from sklearn.datasets import make_blobs

#모의 데이터
features, _ = make_blobs(n_samples = 10,
                         n_features = 2,
                         centers = 1,
                         random_state = 1)

#첫 번째 샘플을 극단적인 값으로 설정
features[0,0] = 10000
features[0,1] = 10000

#이상치 감지 객체
outlier_detector = EllipticEnvelope(contamination=.1)

#감지 객체를 훈련
outlier_detector.fit(features)

#이상치 예측
outlier_detector.predict(features)



feature = features[:,0]

#이상치의 인덱스를 반환하는 함수
def indicies_of_outliers(x):
    q1, q3 = np.percentile(x, [25, 75])
    iqr = q3 - q1
    lower_bound = q1 - (iqr * 1.5)
    upper_bound = q3 + (iqr * 1.5)
    return np.where((x > upper_bound) | (x < lower_bound))

indicies_of_outliers(feature)