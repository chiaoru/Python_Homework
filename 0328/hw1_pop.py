# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 20:24:36 2023

@author: USER
"""

# homework 1

scores = [100,60,70,80,99,100,66]

"""
1. 由使用者輸入分數後，找到就移除(限用pop)，找不到時，要顯示找不到

"""

number = int(input("請輸入欲移除的分數："))
start = 0

if scores.count(number) > 0:
    for i in range(scores.count(number)):
        index = scores.index(number)
        scores.pop(index)
        start = index + 1
    print(scores)
    
else:
    print("找不到此分數!")