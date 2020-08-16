#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 18:41:14 2020

@author: cpprhtn
"""



import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("images/plane_256x256.jpg", cv2.IMREAD_GRAYSCALE)

#이미지 흐리게 함
#픽셀 다운하는 형식으로 함
image_blurry = cv2.blur(image, (5,5))


plt.imshow(image_blurry, cmap="gray"), plt.axis("off")
plt.show()

#이미지를 흐리게 함
image_very_blurry = cv2.blur(image, (100,100))

plt.imshow(image_very_blurry, cmap="gray"), plt.xticks([]), plt.yticks([])
plt.show()

#커널
kernel = np.ones((5,5)) / 25.0

#커널 확인
kernel

#커널 적용
image_kernel = cv2.filter2D(image, -1, kernel)

plt.imshow(image_kernel, cmap="gray"), plt.xticks([]), plt.yticks([])
plt.show()



#가우시안 블러 적용
image_very_blurry = cv2.GaussianBlur(image, (5,5), 0)

plt.imshow(image_very_blurry, cmap="gray"), plt.xticks([]), plt.yticks([])
plt.show()


gaus_vector = cv2.getGaussianKernel(5, 0)
gaus_vector

#벡터를 외적하여 커널 생성
gaus_kernel = np.outer(gaus_vector, gaus_vector)
gaus_kernel

#커널 적용
image_kernel = cv2.filter2D(image, -1, gaus_kernel)

plt.imshow(image_kernel, cmap="gray"), plt.xticks([]), plt.yticks([])
plt.show()