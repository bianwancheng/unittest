#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/3/12 14:06
# @Author  :  wancheng.b
# @Site     :
# @File     : Single01Test.py
# @Software  : PyCharm

import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
