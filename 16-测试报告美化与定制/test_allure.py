#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/2/19 上午11:21
 @Version : 1.0   
 @Description :

 1.只运行登陆模块命令：  pytest -sv test_allure.py  --allure-features="登陆模块"
 2.只运行登陆失败的命令：pytest -sv test_allure.py  --allure-stories="登陆失败"
 3.生成报告：  pytest -sv test_allure.py  --allure-features="登陆模块" -vs --alluredir=./result
   --clean-alluredir 是每次运行都清除原有的报告： pytest -sv test_allure.py  --alluredir=./result --clean-alluredir
 4.生成可视化报告：allure serve ./result

 5.添加链接：  @allure.testcase(TEST_CASE_LINK,'测试链接')

"""
import allure
import pytest


@allure.feature("搜索模块")
class TestSearch():

    def test_case1(self):
        print("case1")

    def test_case2(self):
        print("case2")

@allure.feature("登陆模块")
class TestLogin():

    @allure.story("登陆成功")
    def test_login_success(self):
        with allure.step("步骤1：打开应用"):
            print("打开应用")
        with allure.step("步骤2：进入登陆页面"):
            print("进入登陆页面")
        with allure.step("步骤3：输入用户名和密码"):
            print("输入用户名和密码")
        print("这是登陆：测试用例，登陆成功")
        pass

    @allure.story("登陆失败")
    def test_login_success_a(self):
        print("这是登陆：测试用例，登陆成功")
        pass

    @allure.story("用户名缺少")
    def test_login_success_b(self):
        print("用户名缺少")
        pass

    @allure.story("密码缺失")
    def test_login_failure(self):
        with allure.step("点击用户名"):
            print("输入用户名")
        with allure.step("点击密码"):
            print("输入密码")
        print("点击登陆")

        with allure.step("点击登陆之后失败"):
            assert '1'==1
        print("登陆失败")
        pass

    @allure.story("登陆失败")
    def test_login_failure_a(self):
        print("这是登陆：测试用例，登陆失败")
        pass

    TEST_CASE_LINK="http://www.baidu.com"
    @allure.testcase(TEST_CASE_LINK,'测试链接')
    def test_with_link(self):
        """
        包含连接的测试报告
        :return:
        """
        pass

if __name__ == '__main__':
    pytest.main()