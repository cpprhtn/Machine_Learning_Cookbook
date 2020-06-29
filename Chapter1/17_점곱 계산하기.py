#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 18:59:49 2020

@author: cpprhtn
"""



import numpy as np

vector_a = np.array([1,2,3])
vector_b = np.array([4,5,6])

#점곱 계산
np.dot(vector_a, vector_b)


#@는 np.matmul함수, 이 함수는 np.dot와 달리 넘파이 스칼라 배열에 적용안됨
scalar_a = np.array(1)
scalar_b = np.array(2)
np.dot(scalar_a, scalar_b)

#스칼라 배열에는 적용안됨
scalar_a @ scalar_b