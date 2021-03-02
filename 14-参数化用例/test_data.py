#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/2/19 上午10:30
 @Version : 1.0   
 @Description :
"""
import pytest
import yaml


class TestData():


    @pytest.mark.parametrize(['a','b'],[
        (1,2),(2,3)
    ])
    def test_date(self,a,b):
        print(a+b)
        return a+b


    @pytest.mark.parametrize("a,b",yaml.safe_load(open('./data.yaml','r')))
    def test_yaml(self,a,b):

        print("result=",a+b)
        return True



