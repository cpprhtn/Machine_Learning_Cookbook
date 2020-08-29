#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 20:47:19 2020

@author: cpprhtn
"""



import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, roc_auc_score
from sklearn.model_selection import train_test_split

features, target = make_classification(n_samples=10000,
                                       n_features=10,
                                       n_classes=2,
                                       n_informative=3,
                                       random_state=3)

features_train, features_test, target_train, target_test = train_test_split(
    features, target, test_size=0.1, random_state=1)

logit = LogisticRegression()

logit.fit(features_train, target_train)

target_probabilities = logit.predict_proba(features_test)[:,1]

#진짜 양성 비율과 거짓 양성 비율
false_positive_rate, true_positive_rate, threshold = roc_curve(target_test, target_probabilities)

#ROC 곡선
plt.title("Receiver Operating Characteristic")
plt.plot(false_positive_rate, true_positive_rate)
plt.plot([0, 1], ls="--")
plt.plot([0, 0], [1, 0] , c=".7"), plt.plot([1, 1] , c=".7")
plt.ylabel("True Positive Rate")
plt.xlabel("False Positive Rate")
plt.show()

#예측 확률
logit.predict_proba(features_test)[0:1]

print("임계값:", threshold[116])
print("진짜 양성 비율:", true_positive_rate[116])
print("거짓 양성 비율:", false_positive_rate[116])

print("임계값:", threshold[45])
print("진짜 양성 비율:", true_positive_rate[45])
print("거짓 양성 비율:", false_positive_rate[45])

#ROC 곡선 아래 면적
roc_auc_score(target_test, target_probabilities)


from sklearn.metrics import precision_recall_curve

#진짜 양성 비율과 거짓 양성 비율
precision, recall, threshold = precision_recall_curve(
    target_test, target_probabilities)

plt.title("Precision-Recall Curve")
plt.plot(precision, recall)
plt.plot([0, 1], ls="--")
plt.plot([1, 1], c=".7"), plt.plot([1, 1], [1, 0] , c=".7")
plt.ylabel("Precision")
plt.xlabel("Recall")
plt.show()

from sklearn.metrics import average_precision_score

#평균 정밀도
average_precision_score(target_test, target_probabilities)

cross_validate(logit, features, target, scoring=["roc_auc", "average_precision"])