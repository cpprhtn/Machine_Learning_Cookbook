#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 19:55:04 2020

@author: cpprhtn
"""



import numpy as np

#초깃값 지정
np.random.seed(0)

#0.0과 1.0 사이에서 세 개의 실수 난수 생성
np.random.random(3)

#1과 10 사이에서 세 개의 정수 난수 생성
np.random.randint(0, 11, 3)

#평균이 0.0이고 표준 편차가 1.0인 정규 분포에서 세 개의 수 생성
np.random.normal(0.0, 1.0, 3)

#평균이 0.0이고 스케일이 1.0인 로지스틱 분포에서 세 개의 수 생성
np.random.logistic(0.0, 1.0, 3)

#1.0보다 크거나 같고 2.0보다 작은 세 개의 수 생성
np.random.uniform(1.0, 2.0, 3)


#0.0(포함)과 1.0 사이에서 세 개의 실수 난수를 생성
#np.random.random((2, 3)), np.random.sample((2, 3)), 
#np.random.uniform(0.0, 1.0, (2, 3))과 동일
np.random.random_sample((2, 3))

#rand 함수는 크기를 튜플이 아닌 개별적인 매개변수로 전달
#np.random.random_sample((2, 3))과 동일
np.random.rand(2, 3)

#randint 함수는 최솟값을 포함하고 최댓값은 포함하지 않는 정수 난수를 생성
np.random.randint(0, 1, 10)

#randn 함수는 크기를 튜플이 아닌 개별적인 매개변수로 전달
#np.random.normal(0.0, 1.0, (2, 3))과 동일
np.random.randn(2, 3)

#choice 함수는 배열의 원소 중 랜덤하게 지정된 횟수만큼 샘플 만듬
#0~2 사이의 정수 중 랜덤하게 10번 생성
#np.random.choice(3, 5)와 동일합니다.
np.random.choice([0,1,2], 5)

#shuffle 함수는 배열 섞음
a = np.array([0, 1, 2, 3, 4])
np.random.shuffle(a)

#permutation 함수는 입력된 배열의 복사본을 만들어 섞은 후 반환
np.random.permutation(a)
np.random.permutation(5)
