#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/2/18 下午12:57
 @Version : 1.0   
 @Description :
"""

list_hogwarts=[1,2,3]
list_hogwarts.append(0)
print(list_hogwarts) #在列表末尾添加元素   [1, 2, 3, 0]
print("=============")

list_hogwarts.insert(1,0)
print(list_hogwarts)  #在指定下标处添加元素  [1, 0, 2, 3, 0]
print("=============")

list_hogwarts.remove(1)
print(list_hogwarts)  #删除某一个值而不是索引：[0, 2, 3, 0]
print("=============")

print(list_hogwarts.pop(1)) #删除索引为1的元素，并把元素返回出来， 2
print("=============")

list_hogwarts1=[1,5,7,43,5,8,2,1]
list_hogwarts1.sort()   #按照默认的元素大小升序排列  [1, 1, 2, 5, 5, 7, 8, 43]
print(list_hogwarts1)
print("=============")

list_hogwarts1.sort(reverse=True)  #按照元素大小降序排列  [43, 8, 7, 5, 5, 2, 1, 1]
print(list_hogwarts1)
print("===============")

list_hogwarts2=[1,5,7,43,5,8,2,1]
list_hogwarts2.reverse()  #按照下标的倒叙排列  [1, 2, 8, 5, 43, 7, 5, 1]
print(list_hogwarts2)

