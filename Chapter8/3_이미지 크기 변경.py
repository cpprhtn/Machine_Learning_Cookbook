#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 18:27:29 2020

@author: cpprhtn
"""



import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("images/plane_256x256.jpg", cv2.IMREAD_GRAYSCALE)

#이미지 크기를 50x50 픽셀로 변경
image_50x50 = cv2.resize(image, (50, 50))

plt.imshow(image_50x50, cmap="gray"), plt.axis("off")
plt.show()