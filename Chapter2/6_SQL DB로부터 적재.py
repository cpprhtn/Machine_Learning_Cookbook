#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 22:19:27 2020

@author: cpprhtn
"""


import pandas as pd
from sqlalchemy import create_engine

#데이터베이스에 연결
database_connection = create_engine('sqlite:///sample.db')

#데이터 적재
dataframe = pd.read_sql_query('SELECT * FROM data', database_connection)

dataframe.head(2)

#테이블의 전체 데이터를 가져 옴
dataframe = pd.read_sql_table('data', database_connection)
dataframe.head(2)