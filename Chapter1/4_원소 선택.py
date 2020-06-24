#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 20:40:57 2020

@author: cpprhtn
"""



import numpy as np


vector = np.array([1, 2, 3, 4, 5, 6])


matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

#3번쨰 원소
vector[2]

#2행 2열의 원소
matrix[1,1]

#모든 원소
vector[:]

#0~3까지의 원소
vector[:3]

#3번쨰 이후의 원소
vector[3:]

#마지막 원소
vector[-1]

#1~3행, 모든 열의 원소
matrix[:2,:]

#모든 행의 2열의 원소
matrix[:,1:2]

#1행과 3의 원소
matrix[[0,2]]

# (0, 1), (2, 0) 위치의 원소
matrix[[0,2], [1,0]]

# matrix의 각 원소에 비교 연산자가 적용
mask = matrix > 5
mask

# 불리언 마스크 배열을 사용하여 원소를 선택
matrix[mask]