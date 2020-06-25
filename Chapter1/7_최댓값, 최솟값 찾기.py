#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 21:37:15 2020

@author: cpprhtn
"""



import numpy as np

matrix = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])

#가장 큰 원소 반환
np.max(matrix)

#가장 작은 원소 반환
np.min(matrix)

#각 열에서의 최댓값
np.max(matrix, axis=0)

#각 행에서의 최댓값
np.max(matrix, axis=1)


#keepdims 매개변수를 True로 지정 => 원본 배열의 차원과 동일한 결과
#   원본 배열과 안전하게 브로드캐스팅 연산 가능

#(3, 1) 크기의 열 벡터
vector_column = np.max(matrix, axis=1, keepdims=True)
vector_column

#브로드캐스팅을 이용가
matrix - vector_column