#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 21:25:55 2020

@author: cpprhtn
"""



import pandas as pd

employee_data = {'employee_id': ['1', '2', '3', '4'],
                 'name': ['Amy Jones', 'Allen Keys', 'Alice Bees',
                 'Tim Horton']}
dataframe_employees = pd.DataFrame(employee_data, columns = ['employee_id',
                                                              'name'])


sales_data = {'employee_id': ['3', '4', '5', '6'],
              'total_sales': [23456, 2512, 2345, 1455]}
dataframe_sales = pd.DataFrame(sales_data, columns = ['employee_id',
                                                      'total_sales'])

#데이터프레임 병합
pd.merge(dataframe_employees, dataframe_sales, on='employee_id')

pd.merge(dataframe_employees, dataframe_sales, on='employee_id', how='outer')

pd.merge(dataframe_employees, dataframe_sales, on='employee_id', how='left')

pd.merge(dataframe_employees, dataframe_sales, left_on='employee_id', right_on='employee_id')