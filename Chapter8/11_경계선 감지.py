#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 21:40:08 2020

@author: cpprhtn
"""



import cv2
import numpy as np
from matplotlib import pyplot as plt

image_gray = cv2.imread("images/plane_256x256.jpg", cv2.IMREAD_GRAYSCALE)

#픽셀 강도의 중간값을 계산
median_intensity = np.median(image_gray)

#중간 픽셀 강도에서 위아래 1 표준 편차 떨어진 값을 임계값으로 지정
lower_threshold = int(max(0, (1.0 - 0.33) * median_intensity))
upper_threshold = int(min(255, (1.0 + 0.33) * median_intensity))

#캐니 경계선 감지기를 적용
image_canny = cv2.Canny(image_gray, lower_threshold, upper_threshold)

plt.imshow(i