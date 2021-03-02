#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/2/18 上午11:15
 @Version : 1.0   
 @Description :
"""

'''
if-else语句
'''
# a=1
# if a==0:
#     print("a=0")
# else:
#     print("a!=0")
#

'''
if-elif-else  语句
'''
# a=3
# if a==0:
#     print("a=0")
# elif a==1:
#     print("a=1")
# elif a==2:
#     print("a=2")
# else:
#     print("未知")


'''
分支嵌套
'''
x=3
if x<1:
    y=3*x+1
else:
    if x<3:
        y=x+2
    else:
        y=3*x
print(y)


