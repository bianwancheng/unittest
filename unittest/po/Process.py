#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/3/13 16:12
# @Author  :  wancheng.b
# @Site     : 
# @File     : Process.py
# @Software  : PyCharm
# import unittest
import os
import unittest

from RunAllcase import MyThread
from lib.adbUtils import ADB
from po.Page import getTest_info, operate


class ProcessUnitTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 安装atx和apk
        package_name = getTest_info('test_package_name', 'package_name')
        package_atx = getTest_info('test_package_name', 'package_atx')
        if not ADB().is_install(package_name):
            ADB().install_app(package_name)

        if not ADB().is_install(package_atx):
            os.system('python -m uiautomator2 init')
        else:
            pass

    @classmethod
    def tearDownClass(cls):
        # 返回apk主页面
        ADB().start_activity('com.verifone.adc.presentation.view.activities.MainActivity')

    def testProcess(self):
        # 解析yaml文件并执行对应操作
        operate()

if __name__ == '__main__':
    pass