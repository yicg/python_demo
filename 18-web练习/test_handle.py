#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/3/1 下午9:35
 @Version : 1.0   
 @Description :  多窗口切换测试

"""
from time import sleep

from selenium import webdriver


class TestHandle():
    driver_path = '/Users/yicg/Downloads/chromedrivers/chromedriver'

    def setup(self):
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)  # 隐式等待

    def teardown(self):
        sleep(3)
        self.driver.quit()

    def test_switch_handle(self):
        """
        1.打开百度
        2.点击登陆
        3.弹框中点击立即注册，输入用户名和账号
        4.返回刚刚的登陆，点击登陆
        5.输入用户名和密码
        :return:
        """
        self.driver.get("https://www.baidu.com")
        #点击登陆
        self.driver.find_element_by_xpath('//*[@id="u1"]//a[1]').click()
        #点击立即注册
        self.driver.find_element_by_css_selector('.pass-reglink.pass-link').click()
        #获取当前页面的所有句柄信息
        handles=self.driver.window_handles
        print("after_handles",handles)
        #获取当前页面的句柄
        default_handle=self.driver.current_window_handle
        print("default_handle", default_handle)

        #切换句柄
        for i in handles:
            if default_handle ==i:
                print("不是这个句柄",i)
                continue
            else:
                print("切换到新句柄")
                self.driver.switch_to_window(i)
        #输入注册信息
        self.driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('tester001')#用户名
        self.driver.find_element_by_id('TANGRAM__PSP_4__phone').send_keys('15317063103')#手机号
        self.driver.find_element_by_id('TANGRAM__PSP_4__password').send_keys('123456') #密码
        self.driver.find_element_by_id('TANGRAM__PSP_4__verifyCode').send_keys('1234') #验证
        #点击立即注册
        self.driver.find_element_by_id('TANGRAM__PSP_4__submit').click()
        # 点击弹框取消
        self.driver.find_element_by_id('TANGRAM__PSP_27__confirm_cancel').click()

        #切换到原先默认的句柄
        self.driver.switch_to_window(default_handle)
        #点击登陆
        self.driver.find_element_by_css_selector('.tang-pass-footerBarULogin.pass-link').click()

        #输入登陆信息
        self.driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys('tester001')
        self.driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys('123456')
        #点击登陆按钮
        self.driver.find_element_by_id('TANGRAM__PSP_11__submit').click()

