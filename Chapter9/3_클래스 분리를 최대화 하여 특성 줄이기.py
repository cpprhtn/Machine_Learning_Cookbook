#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 17:45:41 2020

@author: cpprhtn
"""



from sklearn import datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

#붓꽃 데이터셋
iris = datasets.load_iris()
features = iris.data
target = iris.target

#LDA 객체를 만들고 실행하여 특성을 변환
lda = LinearDiscriminantAnalysis(n_components=1)
features_lda = lda.fit(features, target).transform(features)

print("원본 특성 개수:", features.shape[1])
print("줄어든 특성 개수:", features_lda.shape[1])

lda.explained_variance_ratio_

#LDA를 만들고 실행
lda = LinearDiscriminantAnalysis(n_components=None)
features_lda = lda.fit(features, target)

#설명된 분산의 비율이 담긴 배열을 저장
lda_var_ratios = lda.explained_variance_ratio_

def select_n_components(var_ratio, goal_var: float) -> int:
    
    total_variance = 0.0

    
    n_components = 0

    
    for explained_variance in var_ratio:

        #분산 값 누적
        total_variance += explained_variance

        n_components += 1

        if total_variance >= goal_var:
            break

    return n_components

select_n_components(lda_var_ratios, 0.95)