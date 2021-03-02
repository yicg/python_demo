#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/2/19 下午3:04
 @Version : 1.0   
 @Description :
"""
import yaml


def step1():
    print("打开浏览器")
def step2():
    print("注册新账号")
def step3():
    print("登陆新账号")


def steps(path):
    with open(path) as f:
        steps=yaml.safe_load(f)
        if "step1" in steps:
            step1()
        if "step2" in steps:
            step2()
        if "step3" in steps:
            step3()

def test_func():
    steps("./step.yml")
