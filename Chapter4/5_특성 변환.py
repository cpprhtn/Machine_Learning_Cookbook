#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 21:28:48 2020

@author: cpprhtn
"""



import numpy as np
from sklearn.preprocessing import FunctionTransformer

features = np.array([[2, 3],
                     [2, 3],
                     [2, 3]])


def add_ten(x):
    return x + 10

#변환기 객체
ten_transformer = FunctionTransformer(add_ten)

#특성 행렬 변환
ten_transformer.transform(features)


import pandas as pd

df = pd.DataFrame(features, columns=["feature_1", "feature_2"])

df.apply(add_ten)


FunctionTransformer(add_ten, validate=False).transform(np.array([1, 2, 3]))


from sklearn.compose import ColumnTransformer

def add_hundred(x):
    return x + 100

#(이름, 변환기, 열 리스트)로 구성된 튜플의 리스트를 ColumnTransformer에 전달
ct = ColumnTransformer(
    [("add_ten", FunctionTransformer(add_ten, validate=True), ['feature_1']),
     ("add_hundred", FunctionTransformer(add_hundred, validate=True), ['feature_2'])])

ct.fit_transform(df)