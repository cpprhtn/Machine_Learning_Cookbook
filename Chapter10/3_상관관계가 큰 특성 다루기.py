#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 16:26:12 2020

@author: cpprhtn
"""



import pandas as pd
import numpy as np

#상관관계가 큰 두 특성 행렬
features = np.array([[1, 1, 1],
                     [2, 2, 0],
                     [3, 3, 1],
                     [4, 4, 0],
                     [5, 5, 1],
                     [6, 6, 0],
                     [7, 7, 1],
                     [8, 7, 0],
                     [9, 7, 1]])

dataframe = pd.DataFrame(features)

#상관관계 행렬
corr_matrix = dataframe.corr().abs()

#상관관계 행렬의 상삼각(upper triangle) 행렬
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape),
                          k=1).astype(np.bool))

#상관 계수가 0.95보다 큰 특성 열의 인덱스
to_drop = [column for column in upper.columns if any(upper[column] > 0.95)]

#특성 삭제
dataframe.drop(dataframe.columns[to_drop], axis=1).head(3)

dataframe.corr()

np.corrcoef(features, rowvar=False)

np.triu(np.ones((4, 4)), k=2)

np.tril(np.ones((4, 4)), k=0)