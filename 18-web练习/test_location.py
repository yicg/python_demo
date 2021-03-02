#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/2/28 上午10:07
 @Version : 1.0   
 @Description :  定位方式练习
"""
from selenium import webdriver


class TestLocation():
    driver_path = '/Users/yicg/Downloads/chromedrivers/chromedriver'

    def setup(self):
        self.driver=webdriver.Chrome(executable_path=self.driver_path)
        self.driver.get("http://www.baidu.com")
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test(self):
        self.driver.find_element('//*[@id="kw"]').send_keys("霍格沃兹测试学院")
