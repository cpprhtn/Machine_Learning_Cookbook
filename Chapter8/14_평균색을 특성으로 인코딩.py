#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 22:21:20 2020

@author: cpprhtn
"""



import cv2
import numpy as np
from matplotlib import pyplot as plt

image_bgr = cv2.imread("images/plane_256x256.jpg", cv2.IMREAD_COLOR)

#각 채널의 평균을 계산
channels = cv2.mean(image_bgr)

#파랑과 빨강을 바꿈(BGR에서 RGB로 만듭니다)
observation = np.array([(channels[2], channels[1], channels[0])])

#채널 평균 값
observation

plt.imshow(observation), plt.axis("off")
plt.show()