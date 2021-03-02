#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/3/2 下午9:19
 @Version : 1.0   
 @Description :
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains


class TestAlert():
    driver_path = '/Users/yicg/Downloads/chromedrivers/chromedriver'

    def setup(self):
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)  # 隐式等待

    def teardown(self):
        sleep(3)
        self.driver.quit()

    def test_alert(self):
        """
        测试弹框
        1.driver.switch_to_alert()  获取当前页面的警告框
        2.text  获取弹框的文本
        3. accept() 接受现有的警告框（确认按钮)
        4. dismiss() 解散现有警告框（取消按钮）
        5.send_keys(keysToSend="XXX") 发送文本至警告框。keysToSend将文本信息发送至警告框

        :return:
        """
        self.driver.get("http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        #切换一下frame
        self.driver.switch_to_frame("iframeResult")
        #拖动元素
        drag_ele=self.driver.find_element_by_xpath('//*[@id="draggable"]')
        drop_ele=self.driver.find_element_by_xpath('//*[@id="droppable"]')
        action=ActionChains(self.driver)
        action.drag_and_drop(drag_ele,drop_ele).perform()
        sleep(2)
        #获取alert弹框
        alert_ele=self.driver.switch_to_alert()
        print(alert_ele.text)
        #确认弹框
        sleep(3)
        alert_ele.accept()

