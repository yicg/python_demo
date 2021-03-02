#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/2/28 下午3:59
 @Version : 1.0   
 @Description :  模拟鼠标操作时间

 http://sahitest.com/demo/clicks.htm
"""
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestAction():
    driver_path = '/Users/yicg/Downloads/chromedrivers/chromedriver'

    def setup(self):
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)  # 隐式等待

    def teardown(self):
        sleep(3)
        self.driver.quit()

    @pytest.mark.skip
    def test_action(self):
        """
        鼠标点击、双击、右击事件
        :return:
        """
        #鼠标点击
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        click_ele=self.driver.find_element(By.XPATH,'//*[@name="f1"]//input[3]')
        #鼠标双击
        double_click_ele=self.driver.find_element(By.XPATH,'//*[@name="f1"]//input[2]')
        #鼠标右键
        right_click_ele=self.driver.find_element(By.XPATH,'//*[@name="f1"]//input[4]')

        action=ActionChains(self.driver)
        action.click(click_ele)   #单击
        action.double_click(double_click_ele)  #双击
        action.context_click(right_click_ele)  #右键

        action.perform()

    @pytest.mark.skip #忽略执行
    def test_moveto(self):
        """
        鼠标移动
        :return:
        """
        self.driver.get("https://www.baidu.com/")
        moveto_ele=self.driver.find_element(By.XPATH,'//*[@id="s-usersetting-top"]')
        action=ActionChains(self.driver)
        action.move_to_element(moveto_ele)
        action.perform()

    @pytest.mark.skip
    def test_drapdrop(self):
        """
        元素拖拽
        :return:
        """
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drap_ele=self.driver.find_element(By.XPATH,'//*[@id="dragger"]')
        drop_ele=self.driver.find_element(By.XPATH,'/html/body/div[2]')
        action=ActionChains(self.driver)
        action.drag_and_drop(drap_ele,drop_ele)
        action.perform()

    def test_keyboard(self):
        """
        模拟键盘操作
        :return:
        """
        self.driver.get("http://sahitest.com/demo/label.htm")
        self.driver.find_element(By.XPATH,'/html/body/label[1]/input').click()

        action=ActionChains(self.driver)
        action.send_keys("username").pause(1) #pause(1)等待一秒
        action.send_keys(Keys.SPACE).pause(1) #键盘的空格键
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).pause(1)  #键盘的回车键

        action.perform()

