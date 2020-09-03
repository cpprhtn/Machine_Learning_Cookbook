#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 19:02:11 2020

@author: cpprhtn
"""



from sklearn.linear_model import Lasso
from sklearn.datasets import load_boston
from sklearn.preprocessing import StandardScaler

boston = load_boston()
features = boston.data
target = boston.target

scaler = StandardScaler()
features_standardized = scaler.fit_transform(features)

#라쏘 회귀
regression = Lasso(alpha=0.5)

model = regression.fit(features_standardized, target)

#계수
model.coef_

regression_a10 = Lasso(alpha=10)
model_a10 = regression_a10.fit(features_standardized, target)
model_a10.coef_



from sklearn.linear_model import LassoCV

lasso_cv = LassoCV(alphas=[0.1, 1.0, 10.0], cv=5)

model_cv = lasso_cv.fit(features_standardized, target)

model_cv.coef_

model_cv.alpha_

lasso_cv = LassoCV(n_alphas=1000, cv=5)

model_cv = lasso_cv.fit(features_standardized, target)

model_cv.alpha_

lasso_cv.alphas_