#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/3/12 14:06
# @Author  :  wancheng.b
# @Site     : 
# @File     : Single01Test.py
# @Software  : PyCharm
import unittest


class SingleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass()当类中的测试方法被执行前会被调用的一个类方法。该方法只会在类方法前调用，"
              "也就是带有calssmethod装饰器并且没有其他参数的方法。")

    def setUp(self):
        print("每个testCase之前执行setUp")

    def tearDown(self):
        print("每个tesTest执行完执行")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass()当类测试方法被执行完后会被调用的一个类方法。该方法只会在一个类的所有方法执行完成后调用，"
              "该方法被调用时，必须有calssmethod装饰器并且除了类以外没有其他参数的方法。")

    def test_first(self):
        self.assertEqual(8 / 2, 4)
        print("test_first")

    def test_second(self):
        self.assertEqual(1 + 2, 3)
        print("test_second")

    @unittest.skip
    def test_skip(self):
        print("skip")

    @unittest.skipIf(2 + 2 == 4, "成立")
    def test_skipIf(self):
        print("skipIf")

if __name__ == '__main__':
    unittest.main()
