#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/2/18 下午4:31
 @Version : 1.0   
 @Description :
"""
import time

#1.基本操作
print(time.asctime())  # 当前时间的国外时间格式 Thu Feb 18 16:34:19 2021
print(time.time())  #当前时间戳  1613637308.6508229
time.sleep(1)    # 等待时间
print(time.localtime(1613637308.6508229)) #将时间戳转化成带格式的时间元组  time.struct_time(tm_year=2021, tm_mon=2, tm_mday=18, tm_hour=16, tm_min=35, tm_sec=8, tm_wday=3, tm_yday=49, tm_isdst=0)
print(time.localtime())  #当前时间的时间元组
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))  #把当前时间格式化 2021-02-18 16:43:33
print("=================")


#2.获取两天前的时间
#当前时间错
now_timestamp=time.time()
#两天前的时间戳
before_timestamp=now_timestamp-60*60*24*2
#转化成时间元组
tump_time=time.localtime(before_timestamp)
print(time.strftime("%Y-%m-%d %H:%M:%S", tump_time))
print("=================")

