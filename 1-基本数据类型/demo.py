#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/2/18 上午10:55
 @Version : 1.0   
 @Description :
"""

int_a=1
float_a=0.2
compile_a=0.2j   #复数类型

print(type(int_a))
print(type(float_a))
print(type(compile_a))

print("===============")

'''
\n是空格  
aaaa

bbb
'''
str_a='aaaa\n'
print(str_a)
print('bbb')
print("===============")


'''
字符串索引、切片
str_b[0] 打印数组中索引为0的数据  （结果：1）    
str_b[0:5:2]  从下标为0的数开始，到下标为5的数结束，步长为2，其中右区间为开区间，取不到(结果：135)
str_b[0:5]  从下标为0的数开始，到下标为5的数结束，不写步长，默认为1（结果：12345）
str_b[:] 相当于打印所有数组信息  （结果：1234567）
'''
str_b='1234567'
print(str_b)
print(str_b[0])  #1
print(str_b[0:5]) #12345
print(str_b[0:5:2])  #135
print(str_b[:])
print("===============")

'''
列表索引、切片  功能同字符传的功能

1
[1, 3, 5]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5, 6, 7]

'''
list1=[1,2,3,4,5,6,7]
print(list1)
print(list1[0])
print(list1[0:5:2])
print(list1[0:5])
print(list1[:])

print("===============")


