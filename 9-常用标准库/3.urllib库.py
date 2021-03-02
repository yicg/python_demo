#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/2/18 下午4:51
 @Version : 1.0   
 @Description :
"""
import urllib.request

response=urllib.request.urlopen("http://www.baidu.com")

print(response.status)
print(response.headers)