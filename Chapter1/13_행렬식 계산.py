#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 18:05:09 2020

@author: cpprhtn
"""



import numpy as np

matrix = np.array([[1, 2, 3],[2, 4, 6],[3, 8, 9]])

#행렬의 행렬식 반환
np.linalg.det(matrix)