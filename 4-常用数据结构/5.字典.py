#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/2/18 下午1:39
 @Version : 1.0   
 @Description :
"""

#1.字典的定义
'''
<class 'dict'>
{}
<class 'dict'>
{'a': 1, 'b': '1123'}
<class 'dict'>
{'a': 1, 'b': '123'}
'''
dict1={}
dict2={"a":1,"b":"1123"}
dict3=dict(a=1,b="123")
print(type(dict1))
print(dict1)
print(type(dict2))
print(dict2)
print(type(dict3))
print(dict3)
print("====================")

#2.字典操作
a={"a":1,"b":"1123"}
b=dict(a=1,b=2)
print(a.keys())  #取出字典中的所有key值  dict_keys(['a', 'b'])
print(a.values())  # 取出字典中的所有value值  dict_values([1, '1123'])
print("====================")

print(a.pop("a"))  #删除字典中key为a的键值对，并把value的值返回出来 1
print(a.keys())    #dict_keys(['b'])
print("====================")

a1={}
b1=a1.fromkeys([1,2,3])   #分别把列表转成字典，并把1，2，3作为key值，value默认为None   {1: None, 2: None, 3: None}
b2=a1.fromkeys((1,2,3),"a")   #分别把元组转成字典，并把1，2，3作为key值，value为a   {1: 'a', 2: 'a', 3: 'a'}
print(b1)
print(b2)
print("====================")


