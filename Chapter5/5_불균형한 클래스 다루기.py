#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 23:19:21 2020

@author: cpprhtn
"""



import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

iris = load_iris()

#특성 행렬
features = iris.data

#타깃 벡터
target = iris.target

#처음 40개 샘플을 삭제
features = features[40:,:]
target = target[40:]

#클래스 0을 음성 클래스로 하는 이진 타깃 벡터
target = np.where((target == 0), 0, 1)

target

#가중치
weights = {0: .9, 1: 0.1}

#가중치를 부여한 랜덤 포레스트 분류기
RandomForestClassifier(class_weight=weights)

#balanced 클래스 가중치로 랜덤 포레스트 모델을 훈련
RandomForestClassifier(class_weight="balanced")

#각 클래스의 샘플 인덱스를 추출
i_class0 = np.where(target == 0)[0]
i_class1 = np.where(target == 1)[0]

#각 클래스의 샘플 개수
n_class0 = len(i_class0)
n_class1 = len(i_class1)

#클래스 0의 샘플만큼 클래스 1에서 중복을 허용하지 않고 랜덤하게 샘플을 뽑기
#from class 1 without replacement
i_class1_downsampled = np.random.choice(i_class1, size=n_class0, replace=False)

#클래스 0의 타깃 벡터와 다운샘플링된 클래스 1의 타깃 벡터를 합치기
np.hstack((target[i_class0], target[i_class1_downsampled]))

np.vstack((features[i_class0,:], features[i_class1_downsampled,:]))[0:5]

#클래스 1의 샘플 개수만큼 클래스 0에서 중복을 허용하여 랜덤하게 샘플을 선택
i_class0_upsampled = np.random.choice(i_class0, size=n_class1, replace=True)

#클래스 0의 업샘플링된 타깃 벡터와 클래스 1의 타깃 벡터를 합치기
np.concatenate((target[i_class0_upsampled], target[i_class1]))

#클래스 0의 업샘플링된 특성 행렬과 클래스 1의 특성 행렬을 합치기
np.vstack((features[i_class0_upsampled,:], features[i_class1,:]))[0:5]