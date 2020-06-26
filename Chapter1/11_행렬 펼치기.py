#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 20:41:34 2020

@author: cpprhtn
"""



import numpy as np

matrix = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])

#행렬을 1차원 배열로 변환
matrix.flatten()

#행렬을 1차원 벡터로 변환
matrix.reshape(1, -1)

#reshape는 넘파이 배열의 뷰를 반환하지만 flatten 메서드는 새로운 배열을 만듬
vector_reshaped = matrix.reshape(-1)
vector_flattened = matrix.flatten()

#(0, 0) 위치의 원소를 바꿈
matrix[0][0] = -1

#배열의 뷰는 원본 배열의 변경 사항을 반영
vector_reshaped

#복사된 배열에는 영향이 없음
vector_flattened