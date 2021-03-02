#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/2/19 下午2:15
 @Version : 1.0   
 @Description :
"""
import pytest


class TestDemo():
    """
    标签运行:给用例加标签：@pytest.mark.XXX
    1.pytest -sv -m "demo" test_mark.py  只运行标签为demo的用例，不加-m默认是运行所有
    2.pytest -sv -m "demo and smoke" test_mark.py  运行含有这两个标签的用例,and/or
    """

    @pytest.mark.demo
    def test_demo(self):
        print("我的第一个用例")

    @pytest.mark.smoke
    @pytest.mark.demo
    def test_two(self):
        print("我的第二个用例")