#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 20:48:44 2020

@author: cpprhtn
"""



import numpy as np
from sklearn.preprocessing import LabelBinarizer, MultiLabelBinarizer

feature = np.array([["Texas"],
                    ["California"],
                    ["Texas"],
                    ["Delaware"],
                    ["Texas"]])

#원-핫 인코더
one_hot = LabelBinarizer()

#특성을 원-핫 인코딩
one_hot.fit_transform(feature)

#특성의 클래스 확인
one_hot.classes_

#원-핫 인코딩을 되돌리기
one_hot.inverse_transform(one_hot.transform(feature))


import pandas as pd

#특성으로 더미(dummy) 변수를 만듦
pd.get_dummies(feature[:,0])

multiclass_feature = [("Texas", "Florida"),
                      ("California", "Alabama"),
                      ("Texas", "Florida"),
                      ("Delware", "Florida"),
                      ("Texas", "Alabama")]

#다중 클래스 원-핫 인코더
one_hot_multiclass = MultiLabelBinarizer()

#다중 클래스 특성을 원-핫 인코딩
one_hot_multiclass.fit_transform(multiclass_feature)

#클래스 확인
one_hot_multiclass.classes_

 
from sklearn.preprocessing import OneHotEncoder

feature = np.array([["Texas", 1],
                    ["California", 1],
                    ["Texas", 3],
                    ["Delaware", 1],
                    ["Texas", 1]])

one_hot_encoder = OneHotEncoder(sparse=False)
one_hot_encoder.fit_transform(feature)

one_hot_encoder.categories_