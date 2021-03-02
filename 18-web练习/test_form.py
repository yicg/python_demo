#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/2/28 下午5:02
 @Version : 1.0   
 @Description :   测试表单
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestForm():
    driver_path = '/Users/yicg/Downloads/chromedrivers/chromedriver'

    def setup(self):
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)  # 隐式等待

    def teardown(self):
        sleep(3)
        self.driver.quit()

    def test_form(self):
        """
        表单测试,和正常的定位是一样的
        :return:
        """
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element(By.ID,'user_login').send_keys("张三")
        self.driver.find_element(By.ID,'user_password').send_keys("123456")
        self.driver.find_element_by_xpath('//*[@id="user_remember_me"]').click()

