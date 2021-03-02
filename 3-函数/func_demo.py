#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/2/18 下午12:43
 @Version : 1.0   
 @Description :
"""

def fun(a,b,c):
    print("这是一个函数")
    print("这是参数a",a)

    return b

fun(1,2,3)
print("==============")

'''
默认参数
'''
def func1(a=1,b=2,c=3):
    print("参数的值是：",a,b,c)

func1()
func1(b=5,a=6,c=10) #关键字参数
print("==============")
