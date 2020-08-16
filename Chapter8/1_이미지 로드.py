#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 18:05:26 2020

@author: cpprhtn
"""



import cv2
import numpy as np
from matplotlib import pyplot as plt

#흑백 이미지로 로드
image = cv2.imread("images/plane.jpg", cv2.IMREAD_GRAYSCALE)

#이미지 출력
plt.imshow(image, cmap="gray"), plt.axis("off")
plt.show()

type(image)

#컬러로 이미지 로드
image_bgr = cv2.imread("images/plane.jpg", cv2.IMREAD_COLOR)

#픽셀 확인
image_bgr[0,0]


#python은 GBR순서라 RGB순으로 변환해줘야 함
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

plt.imshow(image_rgb), plt.axis("off")
plt.show()