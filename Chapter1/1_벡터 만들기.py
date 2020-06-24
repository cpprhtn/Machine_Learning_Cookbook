#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 19:17:14 2020

@author: cpprhtn
"""



import numpy as np
#1행
vector_row = np.array([1, 2, 3])
vector_row

#1열
vector_column = np.array([[1],[2],[3]])
vector_column

#클래스 출력
print(type(vector_row))


# ndarray를 사용하는 것은 권장되지 않는다고 함
bad_way = np.ndarray((3,))

new_row = np.asarray([1, 2, 3])
# asarray() : 새로운 배열을 만들지 않음 (튜플느낌)
new_row = np.asarray(vector_row)
new_row is vector_row    #Out: True

# array() : 배열이 입력되면 새로운 배열을 만듬
new_row = np.array(vector_row)
new_row is vector_row    #Out: False

# copy() 메서드를 사용하여 의도를 명확히 표현가능
new_row = vector_row.copy()
new_row is vector_row    #Out: False
