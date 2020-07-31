#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 20:31:03 2020

@author: cpprhtn
"""



from bs4 import BeautifulSoup

html = """
       <div class='full_name'><span style='font-weight:bold'>
       Masego</span> Azra</div>"
       """

#html 파싱
soup = BeautifulSoup(html, "lxml")

#"full_name" 이름의 클래스를 가진 div를 찾기
soup.find("div", { "class" : "full_name" }).text