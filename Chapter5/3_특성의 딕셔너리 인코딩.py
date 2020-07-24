#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 21:51:01 2020

@author: cpprhtn
"""



from sklearn.feature_extraction import DictVectorizer

data_dict = [{"Red": 2, "Blue": 4},
             {"Red": 4, "Blue": 3},
             {"Red": 1, "Yellow": 2},
             {"Red": 2, "Yellow": 2}]

#DictVectorizer 객체
dictvectorizer = DictVectorizer(sparse=False)

#딕셔너리를 특성 행렬로 변환
features = dictvectorizer.fit_transform(data_dict)

features

#특성 이름
feature_names = dictvectorizer.get_feature_names()

feature_names #['Blue', 'Red', 'Yellow']


import pandas as pd

pd.DataFrame(features, columns=feature_names)

doc_1_word_count = {"Red": 2, "Blue": 4}
doc_2_word_count = {"Red": 4, "Blue": 3}
doc_3_word_count = {"Red": 1, "Yellow": 2}
doc_4_word_count = {"Red": 2, "Yellow": 2}

doc_word_counts = [doc_1_word_count,
                   doc_2_word_count,
                   doc_3_word_count,
                   doc_4_word_count]

#단어 카운트 딕셔너리를 특성 행렬로 변환
dictvectorizer.fit_transform(doc_word_counts)

