#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 19:30:10 2020

@author: cpprhtn
"""



import numpy as np

matrix_a = np.array([[1, 1],[1, 2]])

matrix_b = np.array([[1, 3],[1, 2]])

#행렬의 곱
np.dot(matrix_a, matrix_b)

#행렬의 곱
matrix_a @ matrix_b

#원소별 곱
matrix_a * matrix_b


#np.dot함수는 다차원 배열에도 적용가능
#이때 첫 번째 배열의 마지막 차원과, 두 번째 배열의 끝에서 두 번째 차원이 동일해야함
#이와 달리 @연산자는 다차원 배열을 마치막 두 차원이 단순히 쌓인 것으로 취급
a = np.random.rand(2, 1, 4, 5)
b = np.random.rand(1, 3, 5, 6)

np.dot(a, b).shape 
#Out: (2, 1, 4, 1, 3, 6)

np.matmul(a, b).shape 
#Out: (2, 3, 4, 6)
