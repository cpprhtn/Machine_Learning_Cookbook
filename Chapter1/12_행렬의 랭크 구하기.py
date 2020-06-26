#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 21:10:21 2020

@author: cpprhtn
"""



import numpy as np

matrix = np.array([[1, 1, 1],[1, 1, 10],[1, 1, 15]])


#행렬의 랭크 : 행이나 열이 만든 벡터 공간의 차원

#행렬의 랭크를 반환
np.linalg.matrix_rank(matrix) #matrix_rank는 특잇값 분해 방식으로 랭크를 계산

#2차원 배열이므로 2 반환
np.ndim(matrix)

#svd 함수로 특잇값만 계산
s = np.linalg.svd(matrix, compute_uv=False)

#오차를 고려하여 0에 가까운 아주 작은 값을 지정
np.sum(s > 1e-10)
