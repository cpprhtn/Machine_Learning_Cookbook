#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 22:09:20 2020

@author: cpprhtn
"""



import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("images/plane_256x256.jpg", cv2.IMREAD_GRAYSCALE)

#이미지를 10x10 픽셀 크기로 변환
image_10x10 = cv2.resize(image, (10, 10))

#이미지 데이터를 1차원 벡터로 변환
image_10x10.flatten()

plt.imshow(image_10x10, cmap="gray"), plt.axis("off")
plt.show()


#컬러 이미지로 로드
image_color = cv2.imread("images/plane_256x256.jpg", cv2.IMREAD_COLOR)

image_color_10x10 = cv2.resize(image_color, (10, 10))

image_color_10x10.flatten().shape

image_256x256_gray = cv2.imread("images/plane_256x256.jpg", cv2.IMREAD_GRAYSCALE)

image_256x256_gray.flatten().shape

image_256x256_color = cv2.imread("images/plane_256x256.jpg", cv2.IMREAD_COLOR)

image_256x256_color.flatten().shape