#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/2/18 下午2:29
 @Version : 1.0   
 @Description :
"""

f=open('./data.txt')
print(f.readable())   #readable()是否可读  True
print(f.read())
f.close()

with open('./data.txt',mode='r') as f:  #使用了with就不用写close函数了
    print(f.read())

