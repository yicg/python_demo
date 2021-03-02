#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/2/18 下午4:15
 @Version : 1.0   
 @Description :
"""

import os

os.mkdir("testdir")   # 在当前路径下创建文件夹
print(os.listdir("./"))  # os.listdir("./")  查看当前文件夹下包含什么文件   ['__init__.py', 'testdir', '1.os模块.py']
os.removedirs("testdir") # 删除当前路径下的文件
print(os.getcwd())  #查看当前文件所在的路径    /Users/yicg/PycharmProjects/python-demo/9-常用标准库

print(os.path.exists("b"))  #判断当前文件夹下是否存在b文件夹

'''
1.判断路径下有没有文件夹b，如果没有，新建一个文件夹b
2.判断文件夹b下有没有test.txt文件，如果没有，新建一个文件，并赋予写权限，写入内容
'''
if not os.path.exists("b"):
    os.mkdir("b")
if not os.path.exists("b/test.txt"):
    f=open("b/test.txt",mode="w")
    f.write("hello os using")
    f.close()