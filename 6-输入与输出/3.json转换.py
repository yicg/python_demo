#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/2/18 下午2:50
 @Version : 1.0   
 @Description :  json是有列表和字典组成的
"""
import json

data={
    "name":["jerry","nickname"],
    "age":26,
    "gender":"male"
}
s1=json.dumps(data)   #把json对象转化成字符串类型
print(type(s1))
print(s1)
print("===============")

s2=json.loads(s1)  #把字符串转化成json对象
print(type(s2))
print(s2)
print("===============")

data3={
    "student1":{
        "name":"jerry",
        "age":26,
        "gender":"male"
    },
    "student2": {
        "name": "jerry",
        "age": 26,
        "gender": "male"
    }
}

print(json.dumps(data3))