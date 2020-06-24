#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 20:16:21 2020

@author: cpprhtn
"""



import numpy as np
from scipy import sparse


matrix = np.array([[0, 0],[0, 1],[3, 0]])

# CSR 행렬
matrix_sparse = sparse.csr_matrix(matrix)

print(matrix_sparse)



matrix_large = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                         [3, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# CSR 행렬
matrix_large_sparse = sparse.csr_matrix(matrix_large)

#행렬 비교
print(matrix_sparse)
print(matrix_large_sparse)


# (data, (row_index, col_index))로 구성된 튜플을 전달
# shape 매개변수에서 0을 포함한 행렬의 전체 크기를 지정 
matrix_sparse_2 = sparse.csr_matrix(([1, 3], ([1, 2], [1, 0])), shape=(3, 10))

print(matrix_sparse_2)

#희소 행렬을 밀집 배열로 변환
print(matrix_sparse_2.toarray())

#todense : np.matrix 객체 반환
matrix_sparse_2.todense()