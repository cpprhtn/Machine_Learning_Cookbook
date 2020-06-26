#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 19:38:57 2020

@author: cpprhtn
"""



import numpy as np

matrix = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])

#행렬 전치
matrix.T

#벡터 전치
np.array([1, 2, 3, 4, 5, 6]).T

#행 벡터 전치
np.array([[1, 2, 3, 4, 5, 6]]).T

#전치는 배열의 차원을 바꾸는것이므로 1차원 배열에는 영향을 미치지 않음
#.T 메서드 대신 transpose 메서드를 사용할 수도 있음
matrix.transpose()

#2x3x2 행렬
matrix = np.array([[[ 1,  2],
                    [ 3,  4],
                    [ 5,  6]],

                   [[ 7,  8],
                    [ 9, 10],
                    [11, 12]]])

# 두 번째와 세 번째 차원을 바꾸어 2x2x3 행렬로 만들기
matrix.transpose((0, 2, 1))