#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 19:35:18 2020

@author: cpprhtn
"""



from sklearn import datasets
from sklearn import metrics
from sklearn.model_selection import KFold, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

digits = datasets.load_digits()

#특성 행렬
features = digits.data

#타깃 벡터
target = digits.target

#표준화 객체
standardizer = StandardScaler()

#로지스틱 회귀
logit = LogisticRegression()

#표준화한 다음 로지스틱 회귀를 실행하는 파이프라인
pipeline = make_pipeline(standardizer, logit)

#k-폴드 교차검증
kf = KFold(n_splits=10, shuffle=True, random_state=1)

cv_results = cross_val_score(pipeline, #파이프라인
                             features, #특성 행렬
                             target, #타깃 벡터
                             cv=kf, #교차 검증 기법
                             scoring="accuracy", #평가 지표
                             n_jobs=-1) #모든 CPU 코어 사용

#평균
cv_results.mean()


from sklearn.model_selection import train_test_split

#훈련 세트와 테스트 세트
features_train, features_test, target_train, target_test = train_test_split(
    features, target, test_size=0.1, random_state=1)

#훈련 세트로 standardizer의 fit 메서드를 호출
standardizer.fit(features_train)

#훈련 세트와 테스트 세트에 모두 적용
features_train_std = standardizer.transform(features_train)
features_test_std = standardizer.transform(features_test)

#파이프라인
pipeline = make_pipeline(standardizer, logit)

cv_results = cross_val_score(pipeline,
                             features,
                             target, 
                             cv=kf,
                             scoring="accuracy",
                             n_jobs=-1) 




from sklearn.model_selection import ShuffleSplit

#ShuffleSplit 분할기
ss = ShuffleSplit(n_splits=10, train_size=0.5, test_size=0.2, random_state=42)

cv_results = cross_val_score(pipeline,
                             features
                             target,
                             cv=ss,
                             scoring="accuracy",
                             n_jobs=-1) 

#평균
cv_results.mean()



from sklearn.model_selection import RepeatedKFold

#RepeatedKFold 분할기
rfk = RepeatedKFold(n_splits=10, n_repeats=5, random_state=42)

cv_results = cross_val_score(pipeline,
                             features,
                             target,
                             cv=rfk,
                             scoring="accuracy", 
                             n_jobs=-1) 

#검증 점수 개수
len(cv_results)