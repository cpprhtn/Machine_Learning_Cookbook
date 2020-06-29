#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 18:14:01 2020

@author: cpprhtn
"""



import numpy as np

matrix = np.array([[1, 2, 3],[2, 4, 6],[3, 8, 9]])

#대각 원소 반환
matrix.diagonal()

#반환된 배열을 변경하려면 복사를 해야 함
a = matrix.diagonal().copy()

a = np.diag(matrix)
print(a)

#1차원 배열이 주어지면 2차원 대각행렬을 만듬
np.diag(a)