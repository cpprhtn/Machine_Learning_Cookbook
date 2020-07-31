#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 20:12:26 2020

@author: cpprhtn
"""



text_data = ["   Interrobang. By Aishwarya Henriette     ",
             "Parking And Going. By Karl Gautier",
             "    Today Is The night. By Jarek Prakash   "]

#공백 문자 제거
strip_whitespace = [string.strip() for string in text_data]
strip_whitespace

#마침표 제거
remove_periods = [string.replace(".", "") for string in strip_whitespace]
remove_periods


#대문자로 변환하는 함수
def capitalizer(string: str) -> str:
    return string.upper()

[capitalizer(string) for string in remove_periods]



import re

#문자열을 X로 바꿔주는 함수
def replace_letters_with_X(string: str) -> str:
    return re.sub(r"[a-zA-Z]", "X", string)

[replace_letters_with_X(string) for string in remove_periods]
