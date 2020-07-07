#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 20:40:19 2020

@author: cpprhtn
"""



import pandas as pd

dataframe = pd.DataFrame()


dataframe['Name'] = ['Jacky Jackson', 'Steven Stevenson']
dataframe['Age'] = [38, 25]
dataframe['Driver'] = [True, False]


dataframe


new_person = pd.Series(['Molly Mooney', 40, True], index=['Name','Age','Driver'])

#열 추가
dataframe.append(new_person, ignore_index=True)