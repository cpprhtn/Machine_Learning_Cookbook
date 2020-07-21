#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 21:09:57 2020

@author: cpprhtn
"""



import pandas as pd

data_a = {'id': ['1', '2', '3'],
          'first': ['Alex', 'Amy', 'Allen'],
          'last': ['Anderson', 'Ackerman', 'Ali']}
dataframe_a = pd.DataFrame(data_a, columns = ['id', 'first', 'last'])


data_b = {'id': ['4', '5', '6'],
          'first': ['Billy', 'Brian', 'Bran'],
          'last': ['Bonder', 'Black', 'Balwner']}
dataframe_b = pd.DataFrame(data_b, columns = ['id', 'first', 'last'])

#행 방향으로 데이터프레임 연결
pd.concat([dataframe_a, dataframe_b], axis=0)

#열 방향으로 데이터프레임 연결
pd.concat([dataframe_a, dataframe_b], axis=1)

#행 만들기
row = pd.Series([10, 'Chris', 'Chillon'], index=['id', 'first', 'last'])

#행 추가
dataframe_a.append(row, ignore_index=True)