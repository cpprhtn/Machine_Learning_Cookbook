#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 20:53:27 2020

@author: cpprhtn
"""



import numpy as np
from sklearn.preprocessing import Normalizer

features = np.array([[0.5, 0.5],
                     [1.1, 3.4],
                     [1.5, 20.2],
                     [1.63, 34.4],
                     [10.9, 3.3]])

#변환기 객체
normalizer = Normalizer(norm="l2")

#특성 행렬 변환
normalizer.transform(features)

#특성 행렬을 변환
features_l2_norm = Normalizer(norm="l2").transform(features)

features_l2_norm

'''
norm에는 2가지 종류가 있음
l1, l2
'''
features_l1_norm = Normalizer(norm="l1").transform(features)

features_l1_norm

print("첫 번째 샘플 값의 합:",
   features_l1_norm[0, 0] + features_l1_norm[0, 1])


#L1 노름을 사용한 변환.
# 각 행(axis=1)을 합한 결과가 2차원 배열로 유지되도록 keepdims를 True로 설정합니다.
features / np.sum(np.abs(features), axis=1, keepdims=True)

#L2 노름을 사용한 변환.
features / np.sqrt(np.sum(np.square(features), axis=1, keepdims=True))

#각 행에서 최댓값으로 나눕니다.
Normalizer(norm="max").transform(features)