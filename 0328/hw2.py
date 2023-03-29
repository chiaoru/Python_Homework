# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 20:45:49 2023

@author: USER
"""

"""
homework 2
2-1. 由使用者分別輸入六個數字，並放入串列中，請用巢狀迴圈進行由大至小排序，並印出結果。
2-2. 如果使用者輸入的數字一樣的話，則不加入，請使用者重新輸入。

"""

number = []

for i in range(6):
    
    a = int(input("請輸入第{}個數字：".format(i+1)))
    if number.count(a) > 0:
        print("已有相同的數字，請重新輸入！")
        a = int(input("請輸入第{}個數字：".format(i+1)))
        number.append(a)
        print(number)
        
    else:    
        number.append(a)
        print(number)

print("排序前為",number)

# 氣泡排序演算法
for a in range(len(number)-1):
    #print(number[a], sep=" ", end=" ")

    for b in range(len(number)-a-1):
        #print(number[b], sep=" ", end=" ")
        if number[b] < number[b+1]:
            number[b], number[b+1] = number[b+1], number[b]
            
print("排序後為：",number)
        


        

