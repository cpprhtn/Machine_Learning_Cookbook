#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 21:19:04 2020

@author: cpprhtn
"""



import pandas as pd

dataframe = pd.DataFrame({"Score": ["Low", "Low", "Medium", "Medium", "High"]})

scale_mapper = {"Low":1,
                "Medium":2,
                "High":3}

#특성을 정수로 변환
dataframe["Score"].replace(scale_mapper)

dataframe = pd.DataFrame({"Score": ["Low",
                                    "Low",
                                    "Medium",
                                    "Medium",
                                    "High",
                                    "Barely More Than Medium"]})

scale_mapper = {"Low":1,
                "Medium":2,
                "Barely More Than Medium": 3,
                "High":4}

dataframe["Score"].replace(scale_mapper)

scale_mapper = {"Low":1,
                "Medium":2,
                "Barely More Than Medium": 2.1,
                "High":3}
dataframe["Score"].replace(scale_mapper)

from sklearn.preprocessing import OrdinalEncoder

features = np.array([["Low", 10],
                     ["High", 50],
                     ["Medium", 3]])

ordinal_encoder = OrdinalEncoder()
ordinal_encoder.fit_transform(features)

ordinal_encoder.categories_

