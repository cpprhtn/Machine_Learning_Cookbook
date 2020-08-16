#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 18:14:40 2020

@author: cpprhtn
"""



import cv2
import numpy as np
from matplotlib import pyplot as plt

#흑백 이미지로 로드
image = cv2.imread("images/plane.jpg", cv2.IMREAD_GRAYSCALE)

#이미지 저장
cv2.imwrite("images/plane_new.jpg", image)