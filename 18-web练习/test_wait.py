#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/2/25 下午9:45
 @Version : 1.0   
 @Description :  显示等待和隐式等待

 driver_path='/Users/yicg/Downloads/chromedrivers/chromedriver'
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait():
    driver_path = '/Users/yicg/Downloads/chromedrivers/chromedriver'

    def setup(self):
        self.driver=webdriver.Chrome(executable_path=self.driver_path)
        self.driver.get("https://www.testing-studio.com/")
        self.driver.implicitly_wait(5) #隐式等待

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        """
        显示等待
        :return:
        """
        #定义一个元素
        def wait(x):
            return len(self.driver.find_elements(By.XPATH,'//*[@class="table-heading"]'))>=1
        WebDriverWait(self.driver,10).until(wait())

        #写法2   expected_conditions.element_to_be_clickable()知道元素可被点击
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(By.XPATH,'//*[@class="table-heading"]'))
        self.driver.find_element(By.XPATH,'XXXX').click()

