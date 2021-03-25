#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/3/3 下午9:57
 @Version : 1.0   
 @Description : 谷歌浏览器debug模式
"""
import sys
from time import sleep

import yaml
from selenium import webdriver


class TestChrome():

    def setup(self):
        # 获取项目路径
        project_path = sys.path[1]
        print(project_path)
        option=webdriver.ChromeOptions()
        option.debugger_address='127.0.0.1:9222'
        #mac电脑的浏览器驱动
        # driver_path=project_path+'/mac_drivers/chromedriver'
        #公司的浏览器驱动
        driver_path=project_path+'/win10_drivers/office_chromedriver'
        print(driver_path)
        self.driver=webdriver.Chrome(executable_path=driver_path,options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        sleep(3)
        self.driver.quit()

    def test_get_cookies(self):
        """
        把cookie信息写入到yaml文件中
        :return:
        """
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#contacts')
        # 获取浏览器cookies信息
        cookies = self.driver.get_cookies()
        print(cookies)
        with open('./cookie.yaml', 'w', encoding='utf-8') as f:
            yaml.dump(cookies, f)


    def test_login_cookie_yaml(self):
        """
        从yaml里去读取cookie进行登陆
        :return:
        """
        #企业微信的扫描登录页
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?')
        with open('./cookie.yaml','r',encoding='utf-8') as f:
            data=yaml.safe_load(f)
        for cookie in data:
            self.driver.add_cookie(cookie)
        self.driver.find_element_by_xpath('//*[@id="menu_contacts"]').click()


