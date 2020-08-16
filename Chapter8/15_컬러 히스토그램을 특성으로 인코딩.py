#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 22:40:34 2020

@author: cpprhtn
"""



import cv2
import numpy as np
from matplotlib import pyplot as plt

image_bgr = cv2.imread("images/plane_256x256.jpg", cv2.IMREAD_COLOR)

image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

features = []

#각 컬러 채널에 대해 히스토그램을 계산
colors = ("r","g","b")

#각 채널을 반복하면서 히스토그램을 계산하고 리스트에 추가
for i, channel in enumerate(colors):
    histogram = cv2.calcHist([image_rgb], # 이미지
                        [i], # 채널 인덱스
                        None, # 마스크 없음
                        [256], # 히스토그램 크기
                        [0,256]) # 범위
    features.extend(histogram)

observation = np.array(features).flatten()

#처음 다섯 개의 특성
observation[0:5]

# RGB 채널 값
image_rgb[0,0]

import pandas as pd

#각 컬러 채널에 대한 히스토그램을 계산
colors = ("r","g","b")

#컬러 채널을 반복하면서 히스토그램을 계산
for i, channel in enumerate(colors):
    histogram = cv2.calcHist([image_rgb], # 이미지
                        [i], # 채널 인덱스
                        None, # 마스크 없음
                        [256], # 히스토그램 크기
                        [0,256]) # 범위
    plt.plot(histogram, color = channel)
    plt.xlim([0,256])

plt.show()