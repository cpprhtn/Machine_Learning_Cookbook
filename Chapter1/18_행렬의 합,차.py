#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 19:13:48 2020

@author: cpprhtn
"""



import numpy as np

matrix_a = np.array([[1, 1, 1],[1, 1, 1],[1, 1, 2]])

matrix_b = np.array([[1, 3, 1],[1, 3, 1],[1, 3, 8]])

#행렬 합
np.add(matrix_a, matrix_b)

#행렬 차
np.subtract(matrix_a, matrix_b)


#+- 연산으로도 가능
matrix_a + matrix_b