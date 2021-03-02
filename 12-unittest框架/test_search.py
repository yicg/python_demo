#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
 @Author :yicg
 @Time : 2021/2/19 上午9:31
 @Version : 1.0   
 @Description :
"""
import unittest


class Search:
    def search_fun(self):
        print("search_fun")
        return True

class TestSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        """
        类级别执行
        :return:
        """
        print("setUpClass")
        cls.search=Search()

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")


    def setUp(self) -> None:
        """
        方法级别执行
        :return:
        """
        print("setUp")

    def tearDown(self) -> None:
        print("tearDown")

    def test_search1(self):
        print("test_search1")
        # search=Search()
        self.search.search_fun()

    def test_search2(self):
        print("test_search2")
        # search = Search()
        self.search.search_fun()

    @unittest.skip  #忽略执行
    def test_search3(self):
        print("test_search3")
        # search = Search()
        self.search.search_fun()

    def test_equal(self):
        print("test_equal")
        self.assertEqual(1,2,msg="不相等")
    def test_not_equal(self):
        print("test_not_equal")
        self.assertNotEqual(1,1,msg="判断不相等")

if __name__ == '__main__':
    unittest.main()