#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 19:42:08 2020

@author: cpprhtn
"""



import numpy as np

matrix = np.array([[1, 2],[1, 2],[1, 2]])
matrix

matrix_object = np.mat([[1, 2],[1, 2],[1, 2]])
matrix_object


# 임의의 값이 채워진 배열
#빈 배열
empty_matrix = np.empty((3, 2))
empty_matrix
#0으로 채워짐
zero_matrix = np.zeros((3, 2))
zero_matrix
#1로 채워짐
one_matrix = np.ones((3, 2))
one_matrix

# 행렬의 덧셈
seven_matrix = np.zeros((3, 2)) + 7

# full() 함수를 사용하는 것이 효율적
seven_matrix = np.full((3, 2), 7)
seven_matrix
