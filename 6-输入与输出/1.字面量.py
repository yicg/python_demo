#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/2/18 下午2:16
 @Version : 1.0   
 @Description :
"""
#1.格式化输出
name='lili'
age=20
print("my name is {},age is {}".format(name,age))   #my name is lili,age is 20
print("======================")

name_list=['zhangsan','lisi','wangwu']
print("my name is {},{},{}".format(*name_list))  #可以传列表、字典等，但是要解包  my name is zhangsan,lisi,wangwu
print("======================")

print(f"name is {name}",name_list)  #推荐使用f，无需解包   name is lili ['zhangsan', 'lisi', 'wangwu']
print(f"name is {name}",*name_list)  #推荐使用f，也可以解包  name is lili zhangsan lisi wangwu
print("======================")

