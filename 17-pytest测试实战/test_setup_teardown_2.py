#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/2/19 下午1:11
 @Version : 1.0   
 @Description :
"""
import pytest

def test_tree():
    print("test_tree")

def test_four():
    print("test_four")

def setup_moudle():
    print("setup_moudle:执行了")

def teardown_moudle():
    print("teardown_moudle:执行了")

class TestClass():

    def setup_class(self):
        print("setup_class：所有用例执行前执行，只执行一次")

    def teardown_class(self):
        print("teardown_class：所有用例执行结束后执行，只执行一次")

    def setup_method(self):
        print("setup:每个用例用例开始")

    def teardown_method(self):
        print("teardown：每个用例执行结束")

    def test_one(self):
        print("test_one")

    def test_two(self):
        print("test_two")