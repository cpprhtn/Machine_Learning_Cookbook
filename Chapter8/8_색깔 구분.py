#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 20:47:10 2020

@author: cpprhtn
"""



import cv2
import numpy as np
from matplotlib import pyplot as plt

image_bgr = cv2.imread('images/plane_256x256.jpg')

#BGR에서 HSV로 변환
image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)

#HSV에서 파랑 값의 범위를 정의
lower_blue = np.array([50,100,50])
upper_blue = np.array([130,255,255])

#마스크
mask = cv2.inRange(image_hsv, lower_blue, upper_blue)

#이미지에 마스크를 적용
image_bgr_masked = cv2.bitwise_and(image_bgr, image_bgr, mask=mask)

#BGR에서 RGB로 변환
image_rgb = cv2.cvtColor(image_bgr_masked, cv2.COLOR_BGR2RGB)

plt.imshow(image_rgb), plt.axis("off")
plt.show()

#마스크 출력
plt.imshow(mask, cmap='gray'), plt.axis("off")
plt.show()