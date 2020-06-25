#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 20:56:07 2020

@author: cpprhtn
"""


import numpy as np


matrix = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]])

#행렬 크기
matrix.shape

#행렬의 원소 개수(행 * 열)
matrix.size

#차원 수
matrix.ndim

#데이터 타입
print(matrix.dtype)

#바이트 크기
print(matrix.itemsize)

#배열 전체의 바이트 크기
print(matrix.nbytes)