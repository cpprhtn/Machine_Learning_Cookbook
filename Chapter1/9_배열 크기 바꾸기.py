#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 19:11:40 2020

@author: cpprhtn
"""



import numpy as np

matrix = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9],[10, 11, 12]])

#(4,3)행렬 -> (2,6)행렬로 변환
matrix.reshape(2, 6)

#변환하는 행렬간의 원소 수가 일치해야 함
matrix.size

#행 하나에 열은 가능한 많게
matrix.reshape(1, -1)

#1차원 배열 반환 (3가지 다 같음)
matrix.reshape(12)
matrix.reshape(-1)
matrix.ravel()