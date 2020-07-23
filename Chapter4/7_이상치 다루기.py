#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 20:18:35 2020

@author: cpprhtn
"""



import pandas as pd

houses = pd.DataFrame()
houses['Price'] = [534433, 392333, 293222, 4322032]
houses['Bathrooms'] = [2, 3.5, 2, 116]
houses['Square_Feet'] = [1500, 2500, 1500, 48000]

#샘플 필터링
houses[houses['Bathrooms'] < 20]

import numpy as np

#불리언 조건을 기반으로 특성 만들기
houses["Outlier"] = np.where(houses["Bathrooms"] < 20, 0, 1)

#로그 특성
houses["Log_Of_Square_Feet"] = [np.log(x) for x in houses["Square_Feet"]]

houses