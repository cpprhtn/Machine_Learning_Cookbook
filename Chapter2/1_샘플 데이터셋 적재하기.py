#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 22:58:10 2020

@author: cpprhtn
"""


'''

load_boston
보스턴 주택 가격

load_iris
붓꽃 샘플 치수

load_digits
손글씨 데이터셋

'''
from sklearn import datasets

#숫자 데이터셋을 적재
digits = datasets.load_digits()

#특성 행렬
features = digits.data

#타깃 벡터
target = digits.target

#첫 번째 샘플 확인
features[0]

#파이썬 딕셔너리와 유사한 클래스 객체 반환
digits.keys()

#DESCR 키는 데이터셋에 대한 설명을 담고 있음
digits['DESCR'][:70]

import numpy as np

#0에서부터 4까지 다섯 개의 숫자만 적재
X, y = datasets.load_digits(n_class=5, return_X_y=True)
#배열에 있는 고유한 값 반환
np.unique(y)
