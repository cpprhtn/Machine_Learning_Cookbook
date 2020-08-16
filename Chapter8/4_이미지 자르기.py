#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 18:35:59 2020

@author: cpprhtn
"""



import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("images/plane_256x256.jpg", cv2.IMREAD_GRAYSCALE)

#열의 처음 절반과 모든 행을 선택
#절반으로 자르기
image_cropped = image[:,:128]

plt.imshow(image_cropped, cmap="gray"), plt.axis("off")
plt.show()