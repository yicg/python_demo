#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/2/18 下午1:12
 @Version : 1.0   
 @Description :
"""
#1.元组定义
tuple_hogwarts1=(1,2,3)
tuple_hogwarts2=1,2,3
tuple_hogwarts3=(1,2,3,)
print(type(tuple_hogwarts1))
print(type(tuple_hogwarts2))
print(type(tuple_hogwarts3))
print("================")

#2.元组的不可变特性
# list_hogwarts=[1,2,3]
# list_hogwarts[0]="a"
# print(list_hogwarts)  #列表的可变
# print("================")
#
# tuple_hog1=(1,2,3)
# tuple_hog1[0]="a"
# print(tuple_hog1) #元组会报错
# print("================")

#3.列表可以嵌套在元组中
list_a=[1,2,3]
tuple1=(1,2,list_a)
print(tuple1)    # (1, 2, [1, 2, 3])
print("================")
#修改嵌套内的列表元素,tuple1[2][0]意思是元组中的第三个元素的第一个元素
tuple1[2][0]="a"
print(tuple1)  #  (1, 2, ['a', 2, 3])
print("================")

#4.元组的内置函数
a=(1,3,4,5,6,2,"a","b","c","a")
print(a.count("a"))  #元素a在元组中出现的次数  2
print(a.index("a")) #元素a在元组中第一次出现时的索引位置  6
