#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/2/18 下午3:40
 @Version : 1.0   
 @Description :
"""

class Person():
    name='default'
    age=0
    gender='male'
    weight=0

    def __init__(self,name,age,gender,weight):
        print("init method")
        self.name=name
        self.age=age
        self.gender=gender
        self.weight=weight

    def set_name(self,name):
        self.name=name

    def eat(self):
        print("eating")

    def play(self):
        print("palying")

    def jump(self):
        print("jumping")


zs=Person(name="张三",age=26,gender="男",weight=200)
#zs.set_name("张三")
zs.play()
print(zs.name)
print(zs.gender)