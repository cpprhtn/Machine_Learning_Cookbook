#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 20:27:22 2020

@author: cpprhtn
"""



from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification

#특성 행렬과 타깃 벡터
X, y = make_classification(n_samples = 10000,
                           n_features = 3,
                           n_informative = 3,
                           n_redundant = 0,
                           n_classes = 2,
                           random_state = 1)

logit = LogisticRegression()

#정확도를 사용한 교차검증
cross_val_score(logit, X, y, scoring="accuracy")

#정밀도를 사용한 교차검증
cross_val_score(logit, X, y, scoring="precision")

#재현율을 사용한 교차검증
cross_val_score(logit, X, y, scoring="recall")

#f1 점수를 사용한 교차검증
cross_val_score(logit, X, y, scoring="f1")


from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.1,
                                                    random_state=1)

#테스트 세트의 예측
y_hat = logit.fit(X_train, y_train).predict(X_test)

#정확도를 계산합니다.
accuracy_score(y_test, y_hat)


from sklearn.model_selection import cross_validate

#정확도와 정밀도를 사용한 교차검증
cross_validate(logit, X, y, scoring=["accuracy", "precision"])

