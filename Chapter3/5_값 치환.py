#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 20:47:17 2020

@author: cpprhtn
"""



import pandas as pd

url = 'https://tinyurl.com/titanic-csv'

dataframe = pd.read_csv(url)

#값을 치환하고 두 개의 행 출력
dataframe['Sex'].replace("female", "Woman").head(2)

#"female"과 "male을 "Woman"과 "Man"으로 치환
dataframe['Sex'].replace(["female", "male"], ["Woman", "Man"]).head(5)

#값을 치환하고 두 개의 행을 출력
dataframe.replace(1, "One").head(2)

#값을 치환하고 두 개의 행을 출력
dataframe.replace(r"1st", "First", regex=True).head(2)

#female과 male을 person으로 바꿈
dataframe.replace(["female", "male"], "person").head(3)

#female을 1로 바꾸고 male을 0으로 바꿈
dataframe.replace({"female": 1, "male": 0}).head(3)