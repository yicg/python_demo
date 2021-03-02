#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/2/28 下午4:42
 @Version : 1.0   
 @Description :
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By


class TestTouchAction():
    driver_path = '/Users/yicg/Downloads/chromedrivers/chromedriver'

    def setup(self):
        option=webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        #添加这个option是为了防止报：  E selenium.common.exceptions.WebDriverException: Message: unknown command: Cannot call non W3C standard command while in W3C mode

        self.driver = webdriver.Chrome(executable_path=self.driver_path,options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)  # 隐式等待

    def teardown(self):
        sleep(5)
        self.driver.quit()

    def test_touchAction(self):
        """
        对H5操作的touchAction，类似于action

        1.打开浏览器，输入百度
        2.搜索selenium测试
        3.通过TouchAction点击搜索框
        滑动到底部，点击下一页
        关闭chrome浏览器
        :return:
        """
        self.driver.get("http://www.baidu.com")
        #输入搜索内容
        serch_input_ele=self.driver.find_element(By.ID,'kw')
        #点击搜索
        search_ele=self.driver.find_element(By.ID,"su")
        serch_input_ele.send_keys("selenium测试")

        action=TouchActions(self.driver)
        action.tap(search_ele)
        action.perform()
        #滑动,从搜索框的地方开始滑动
        action.scroll_from_element(serch_input_ele,0,10000).perform()
        #action.scroll(0,10000).perform()
