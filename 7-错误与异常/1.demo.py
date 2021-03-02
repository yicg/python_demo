#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/2/18 下午3:16
 @Version : 1.0   
 @Description :
"""

#1.手动触发异常
def set_age(num):
    if num<0 or num>200:
        raise ValueError(f"输入的年龄不符合{num}")
    else:
        print("年龄是，{}".format(num))

set_age(-1)