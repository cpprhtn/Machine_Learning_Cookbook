#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 19:39:31 2020

@author: cpprhtn
"""



import numpy as np

matrix = np.array([[1, 4],
                   [2, 5]])

#역행렬
np.linalg.inv(matrix)

#행렬과 역행렬의 곱
matrix @ np.linalg.inv(matrix)

#pinv 함수를 사용하면 정방행렬이 아닌 행렬의 역행렬을 계산할 수 있음
#이를 유사 역행렬이라 부름
matrix = np.array([[1, 4, 7],[2, 5, 8]])

#유사 역행렬
np.linalg.pinv(matrix)
