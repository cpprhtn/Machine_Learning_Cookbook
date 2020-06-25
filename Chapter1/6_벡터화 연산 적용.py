#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 21:17:20 2020

@author: cpprhtn
"""



import numpy as np


matrix = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])

#모든 원소에 100더하기
add_100 = lambda i: i + 100
    #matrix + 100
    #matrix + [100, 100, 100]
    #matrix + [[100], [100], [100]]

#벡터화된 함수
vectorized_add_100 = np.vectorize(add_100)

#행렬의 모든 원소에 함수를 적용
vectorized_add_100(matrix)

