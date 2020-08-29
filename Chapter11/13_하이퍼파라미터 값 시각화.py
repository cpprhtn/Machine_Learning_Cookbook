#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 23:06:31 2020

@author: cpprhtn
"""



import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import validation_curve

digits = load_digits()

features, target = digits.data, digits.target

#파라미터 값의 범위
param_range = np.arange(1, 250, 2)

train_scores, test_scores = validation_curve(
    RandomForestClassifier(),
    features,
    target,
    #조사할 하이퍼파라미터
    param_name="n_estimators",
    #하이퍼파라미터 값의 범위
    param_range=param_range,
    cv=3,
    scoring="accuracy",
    n_jobs=-1)

#평균과 표준 편차
train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)

test_mean = np.mean(test_scores, axis=1)
test_std = np.std(test_scores, axis=1)

#평균 정확도 점수
plt.plot(param_range, train_mean, label="Training score", color="black")
plt.plot(param_range, test_mean, label="Cross-validation score", color="dimgrey")

#정확도에 대한 표준 편차
plt.fill_between(param_range, train_mean - train_std,
                 train_mean + train_std, color="gray")
plt.fill_between(param_range, test_mean - test_std,
                 test_mean + test_std, color="gainsboro")

plt.title("Validation Curve With Random Forest")
plt.xlabel("Number Of Trees")
plt.ylabel("Accuracy Score")
plt.tight_layout()
plt.legend(loc="best")
plt.show()