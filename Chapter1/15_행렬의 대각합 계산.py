#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 18:26:46 2020

@author: cpprhtn
"""



import numpy as np

matrix = np.array([[1, 2, 3],[2, 4, 6],[3, 8, 9]])

#대각합 반환
matrix.trace()

#대각 원소를 사용하여 합 구하
sum(matrix.diagonal())

#주 대각선 하나 위의 대각 원소의 합을 반환
matrix.trace(offset=1)
#하나 아래의 대각 원소의 합을 반환
matrix.trace(offset=-1)