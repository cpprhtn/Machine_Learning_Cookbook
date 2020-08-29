#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 22:35:16 2020

@author: cpprhtn
"""



from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

iris = datasets.load_iris()

features = iris.data

target = iris.target

class_names = iris.target_names

features_train, features_test, target_train, target_test = train_test_split(
    features, target, random_state=1)

classifier = LogisticRegression()

model = classifier.fit(features_train, target_train)
target_predicted = model.predict(features_test)

#분류 리포트
print(classification_report(target_test,
                            target_predicted,
                            target_names=class_names))


print(classification_report(target_test,
                            target_predicted,
                            labels=[0,1,2,3]))