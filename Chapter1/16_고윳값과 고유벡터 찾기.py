#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 18:42:30 2020

@author: cpprhtn
"""



import numpy as np

matrix = np.array([[1, -1, 3],[1, 1, 6],[3, 8, 9]])

#고윳값과 고유벡터를 계산
eigenvalues, eigenvectors = np.linalg.eig(matrix)
#고윳값 확인
eigenvalues

#고유벡터 확인
eigenvectors

#대칭 행렬
matrix = np.array([[1, -1, 3],[-1, 1, 6],[3, 6, 9]])

#고윳값과 고유벡터를 계산
eigenvalues, eigenvectors = np.linalg.eigh(matrix)