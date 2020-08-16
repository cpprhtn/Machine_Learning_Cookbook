#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 21:26:03 2020

@author: cpprhtn
"""



import cv2
import numpy as np
from matplotlib import pyplot as plt

image_bgr = cv2.imread('images/plane_256x256.jpg')
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

#사각형 좌표: 시작점의 x, 시작점의 y, 너비, 높이
rectangle = (0, 56, 256, 150)

#초기 마스크
mask = np.zeros(image_rgb.shape[:2], np.uint8)

#grabCut에 사용할 임시 배열
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

#grabCut 실행
cv2.grabCut(image_rgb, # 원본 이미지
            mask, # 마스크
            rectangle, # 사각형
            bgdModel, # 배경을 위한 임시 배열
            fgdModel, # 전경을 위한 임시 배열
            5, # 반복 횟수
            cv2.GC_INIT_WITH_RECT) # 사각형을 사용한 초기화

#배경인 곳은 0, 그외에는 1로 설정한 마스크
mask_2 = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')

#이미지에 새로운 마스크를 곱해 배경을 제외
image_rgb_nobg = image_rgb * mask_2[:, :, np.newaxis]

plt.imshow(image_rgb_nobg), plt.axis("off")
plt.show()

#마스크 출력
plt.imshow(mask, cmap='gray'), plt.axis("off")
plt.show()

plt.imshow(mask_2, cmap='gray'), plt.axis("off")
plt.show()