#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 22:17:20 2020

@author: cpprhtn
"""



import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_digits
from sklearn.model_selection import learning_curve

digits = load_digits()

features, target = digits.data, digits.target

train_sizes, train_scores, test_scores = learning_curve(#분류기
                                                        RandomForestClassifier(),
                                                        #특성 행렬
                                                        features,
                                                        #타깃 벡터
                                                        target,
                                                        #폴드 수
                                                        cv=10,
                                                        #성능 지표
                                                        scoring='accuracy',
                                                        #모든 코어 사용
                                                        n_jobs=-1,
                                                        #50개의 훈련 세트 크기
                                                       train_sizes=np.linspace(
                                                       0.01,
                                                       1.0,
                                                       50))

#평균과 표준 편차
train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)

test_mean = np.mean(test_scores, axis=1)
test_std = np.std(test_scores, axis=1)

plt.plot(train_sizes, train_mean, '--', color="#111111",  label="Training score")
plt.plot(train_sizes, test_mean, color="#111111", label="Cross-validation score")

#표준 편차 영역
plt.fill_between(train_sizes, train_mean - train_std,
                 train_mean + train_std, color="#DDDDDD")
plt.fill_between(train_sizes, test_mean - test_std,
                 test_mean + test_std, color="#DDDDDD")

plt.title("Learning Curve")
plt.xlabel("Training Set Size"), plt.ylabel("Accuracy Score"),
plt.legend(loc="best")
plt.tight_layout()
plt.show()