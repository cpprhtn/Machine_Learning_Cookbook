#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 18:45:58 2020

@author: cpprhtn
"""



import numpy as np

matrix = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])

#평균
np.mean(matrix)

#분산
np.var(matrix)

#표준 편차
np.std(matrix)

#각 열의 평균
np.mean(matrix, axis=0)

#편향되지 않은 분산과 표준편차 추정값 (ddof 기본값 : 0)
np.std(matrix, ddof=1)

import pandas as pd

df = pd.DataFrame(matrix.flatten())
df.std() #(ddof 기본값 : 1)