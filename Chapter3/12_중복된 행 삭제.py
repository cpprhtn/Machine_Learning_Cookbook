#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 18:00:09 2020

@author: cpprhtn
"""



import pandas as pd

url = 'https://tinyurl.com/titanic-csv'

dataframe = pd.read_csv(url)

#중복 행을 삭제
dataframe.drop_duplicates().head(2)

#행의 개수를 출력
print("원본 데이터프레임 행의 수:", len(dataframe))
print("중복 삭제 후 행의 수:", len(dataframe.drop_duplicates()))

#중복된 행 삭제
dataframe.drop_duplicates(subset=['Sex'])

#중복된 행 삭제
dataframe.drop_duplicates(subset=['Sex'], keep='last')