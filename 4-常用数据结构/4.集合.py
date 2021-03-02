#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/2/18 下午1:27
 @Version : 1.0   
 @Description :   集合是无需的不重复元素
 创建方式：{}  或者set()
 如果创建一个空集合，只能用set()，而不能用{}

"""

#1.定义集合
a={1}
b=set()
print(type(a))
print(a)
print(type(b))
print(b)
print("=============")


#2.集合基本操作
a1={1,2,3}
b1={1,4,5}
print(a1.union(b1))  #求集合的并集  {1, 2, 3, 4, 5}
print("=============")

print(a1.intersection(b1)) #求集合的交集  {1}
print("=============")

print(a1.difference(b1))  #求集合的差集，就是a1中有的在b1中没有的元素  {2, 3}
print("=============")

a1.add(6)
print(a1)  #添加元素  {1, 2, 3, 6}
print("=============")

#3.集合去重，直接调用set函数
a2="qwertyqaawerqwesd"
print(set(a2))   #数组转化成集合，去重   {'y', 't', 'a', 'd', 'w', 's', 'q', 'r', 'e'}




