#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/2/19 下午12:58
 @Version : 1.0   
 @Description :
"""
import pytest


def add_function(a,b):
    return a+b


@pytest.mark.parametrize("a,b,expected",[
    (1,2,3),(-2,-3,-5),(3.5,5.5,9.0)
],ids=["data1","data2","data3"])
def test_add1(a,b,expected):
    """
    ids=[]是显示别名
    :param a:
    :param b:
    :param expected:
    :return:
    """
    print(f"a、b的值分别是{a},{b}")
    assert add_function(a,b)==expected

@pytest.mark.parametrize("a",[2,3])
@pytest.mark.parametrize("b",[4,5])
def test_add2(a,b):
    """
    参数的组合显示
    :param a:
    :param b:
    :param expected:
    :return:

    a、b的值分别是2,4
    a、b的值分别是3,4
    a、b的值分别是2,5
    a、b的值分别是3,5
    """
    print(f"a、b的值分别是{a},{b}")
