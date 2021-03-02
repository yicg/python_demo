#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/3/1 下午10:11
 @Version : 1.0   
 @Description : 测试frame表单
"""
from time import sleep

from selenium import webdriver


class TestFrame():
    driver_path = '/Users/yicg/Downloads/chromedrivers/chromedriver'

    def setup(self):
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)  # 隐式等待

    def teardown(self):
        sleep(3)
        self.driver.quit()

    def test_frame(self):
        """
        处理嵌套的frame
         1.self.driver.switch_to.frame()   根据元素id或者index切换新的frame
         2.self.driver.switch_to.default_content()  切换到默认的frame
         3.self.driver.switch_to.parent_frame() 切换到父级frame
         处理未嵌套的frame
         1.self.driver.switch_to_frame("frame的id")
         2.self.driver.switch_to_frame("frame-index") frame无ID的时候依据索引来处理，索引从0开始
            driver.switch_to_frame(0)
        :return:
        """
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        #定位到frame下
        self.driver.switch_to.frame("iframeResult")
        print(self.driver.find_element_by_id('draggable').text)



