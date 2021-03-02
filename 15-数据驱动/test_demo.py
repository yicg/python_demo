#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/2/19 上午10:43
 @Version : 1.0   
 @Description :
"""
import pytest
import yaml


class TestDemo():

    @pytest.mark.parametrize("env",yaml.safe_load(open("./env.yaml")))
    def test_data(self,env):
        if "test" in env:
            print("测试环境运行")
        elif "dev" in env:
            print("dev环境运行")
        else:
            print("正式环境运行")

    def test_yaml(self):
        print(yaml.safe_load(open("./env.yaml")))
        f=yaml.safe_load(open("./env.yaml"))  # [{'test': '192.168.0.110'}]
        print(f[0].get("test"))  #取出字典的值    192.168.0.110
        print(f[0]["test"])   #取出字典的值第二种写法    192.168.0.110
