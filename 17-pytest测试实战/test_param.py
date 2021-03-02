#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/2/19 下午2:40
 @Version : 1.0   
 @Description :
"""
import pytest
import yaml


class TestData():

    @pytest.mark.parametrize("a,b,expected",yaml.safe_load(open('./param.yml','r')))
    def test_yaml(self,a,b,expected):

        print("result=",a+b)
        assert (a+b)==expected


    def get_datas(self):
        with open("./param.yml") as f:
            datas=yaml.safe_load(f)
            print(datas)

        return datas


