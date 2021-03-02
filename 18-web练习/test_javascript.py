#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/3/1 下午10:27
 @Version : 1.0   
 @Description :   测试script
"""
from time import sleep

from selenium import webdriver


class TestJs():
    driver_path = '/Users/yicg/Downloads/chromedrivers/chromedriver'

    def setup(self):
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)  # 隐式等待

    def teardown(self):
        sleep(3)
        self.driver.quit()

    def test_js_1(self):
        """
        案例1：滑动到浏览器底部或者顶部
        1.打开百度首页
        2.输入搜索关键字
        3.点击搜索后，跳转到搜索结果页
        4.滑动到底部点击下一页

        :return:
        """
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        ele=self.driver.execute_script("return document.getElementById('su')")  #js
        ele.click()
        sleep(3)
        #滑动到最低端
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        #点击下一页
        self.driver.find_element_by_xpath('//*[@class="n"]').click()
        sleep(3)
        #在滑一次
        self.driver.execute_script("document.documentElement.scrollTop=10000")

    def test_js_2(self):
        """
        js案例2
        1.打开12306网站
        2.移除时间的只读模式
        3.输入新的时间
        :return:
        """
        self.driver.get("https://www.12306.cn/index/")
        #移除只读模式
        self.driver.execute_script(" a=document.getElementById('train_date');a.removeAttribute('readonly');")
        #输入新的时间
        self.driver.execute_script("a=document.getElementById('train_date');a.value='2020-3-20'")