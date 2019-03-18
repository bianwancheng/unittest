#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/3/13 16:12
# @Author  :  wancheng.b
# @Site     : 
# @File     : Process.py
# @Software  : PyCharm
# import unittestAuto
import os

from unittestAuto.lib.adbUtils import ADB
from unittestAuto.po.Page import operate
from unittestAuto.public.PageMethod import getTest_info, existCase


class Process:

    @classmethod
    def beforeClass(cls):
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
    def afterClass(cls):
        # 返回apk主页面
        ADB().start_activity('com.verifone.adc.presentation.view.activities.MainActivity')

    def runAllCase(self, driver):
        # 解析yaml文件并执行对应操作
        self.beforeClass()
        allyamlsList = existCase(getTest_info('test_case', 'caseYaml'))
        operate(driver, allyamlsList)
        self.afterClass()

    def runOneCase(self, driver, casePath):
        # 解析yaml文件并执行对应操作
        self.beforeClass()
        oneYaml = []
        oneYaml.append(casePath)
        operate(driver, oneYaml)
        self.afterClass()


if __name__ == '__main__':
    pass
