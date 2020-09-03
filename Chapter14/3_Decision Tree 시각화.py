#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 19:40:15 2020

@author: cpprhtn
"""



import pydotplus
from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets
from IPython.display import Image
from sklearn import tree

iris = datasets.load_iris()
features = iris.data
target = iris.target

decisiontree = DecisionTreeClassifier(random_state=0)

model = decisiontree.fit(features, target)

dot_data = tree.export_graphviz(decisiontree,
                                out_file=None,
                                feature_names=iris.feature_names,
                                class_names=iris.target_names)

graph = pydotplus.graph_from_dot_data(dot_data)

#그래프 출력
Image(graph.create_png())

#PDF 파일
graph.write_pdf("iris.pdf")

#PNG 파일
graph.write_png("iris.png")




'''
pyplot로 출력가능
'''
import matplotlib.pyplot as plt

plt.figure(figsize=(20, 15))
tree.plot_tree(model, filled=True, 
               feature_names=iris.feature_names,
               class_names=iris.target_names,
               rounded=True, fontsize=14)
plt.show()