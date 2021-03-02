#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/3/2 下午9:08
 @Version : 1.0   
 @Description :   图片上传
"""
from time import sleep

from selenium import webdriver


class TestUpload():
    driver_path = '/Users/yicg/Downloads/chromedrivers/chromedriver'

    def setup(self):
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)  # 隐式等待

    def teardown(self):
        sleep(3)
        self.driver.quit()

    def test_upload_image(self):
        """
        图片上传
        1.打开百度图片网站
        2.识别上传按钮
        3.点击上传按钮
        4.将本地的图片文件上传
        :return:
        """
        self.driver.get("https://image.baidu.com/")
        #点击图片上传按钮
        self.driver.find_element_by_xpath('//*[@id="sttb"]').click()
        #选择图片
        self.driver.find_element_by_xpath('uploadImg').send_keys('/Users/yicg/Desktop/123.png')

