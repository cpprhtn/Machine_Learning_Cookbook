#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 20:34:32 2020

@author: cpprhtn
"""



import numpy as np
from sklearn.preprocessing import Binarizer

age = np.array([[6],
                [12],
                [20],
                [36],
                [65]])

#Binarizer 객체
binarizer = Binarizer(threshold=18)

#특성 변환
binarizer.fit_transform(age)

#특성 나누기
np.digitize(age, bins=[20,30,64])
'''
array([[0],
       [0],
       [1],
       [2],
       [3]])
'''

np.digitize(age, bins=[20,30,64], right=True)
'''
array([[0],
       [0],
       [0],
       [2],
       [3]])
'''

np.digitize(age, bins=[18])
'''
array([[0],
       [0],
       [1],
       [1],
       [1]])
'''

from sklearn.preprocessing import KBinsDiscretizer

#4구간으로 나누기
kb = KBinsDiscretizer(4, encode='ordinal', strategy='quantile')
kb.fit_transform(age)

#원-핫 인코딩 반환
kb = KBinsDiscretizer(4, encode='onehot-dense', strategy='quantile')
kb.fit_transform(age)

#동일한 길이의 구간
kb = KBinsDiscretizer(4, encode='onehot-dense', strategy='uniform')
kb.fit_transform(age)


kb.bin_edges_
#array([array([ 6.  , 20.75, 35.5 , 50.25, 65.  ])], dtype=object)