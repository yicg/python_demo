#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/2/18 上午11:28
 @Version : 1.0   
 @Description :
"""
import random

'''
for循环语句
range(100):产生一个0到90的整数序列，100开区间
range(1,100)：产生一个1到99的整数序列
range(1,100,2)：产生一个1到99的奇数序列，2是步长

1.计算1-100的求和
2.计算1-100的偶数和
'''
result1=0
for i in range(101):
    result1=result1+i
print(result1)
print('=============')

result2=0
for i in range(2,101,2):
    result2=result2+i;
print(result2)
print('=============')

'''
while循环
'''
a=1
while a==1:
    a=a+1
    print("result",a)
else:
    print("a!=1，退出循环")
print('=============')

'''
break continue
'''
for i in range(1,10):
    print(i)
    if i==5:
        break
print('=============')

'''
猜数字游戏
random.randint(1,100)  1，100的随机数
'''

computer_num=random.randint(1,100)
print(computer_num)
while True:
    person_num = int(input("请输入数字"))
    if person_num>computer_num:
        print("你输入的数子太大啦！！")
    elif person_num<computer_num:
        print("你输入的数字太小啦！！！")
    else:
        print("猜对啦，哈哈哈")
        print(person_num)
        break
