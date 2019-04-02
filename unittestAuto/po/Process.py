#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/3/13 16:12
# @Author  :  wancheng.b
# @Site     : 
# @File     : Process.py
# @Software  : PyCharm
# import unittestAuto
import os
import time
from unittestAuto.lib.adbUtils import ADB
from unittestAuto.po.Page import PagePo
from unittestAuto.public.LogUtils import Logging
from unittestAuto.public.PageMethod import getTest_info, existCase, mkdir_file


class Process:
    def __init__(self, device):
        self.device = device
        self.time = time.strftime(
            "%Y-%m-%d_%H_%M_%S",
            time.localtime(
                time.time()))
        # mkdirLog()
        pass

        # mkdirLog()
        # Logging.info('创建设备驱动')
        # driver = u2.connect(self.device)
        # Logging.info('执行所有用例')
        # Process().runAllCase(driver)


    @classmethod
    def beforeClass(cls):
        '''
        安装atx和apk

        :return:
        '''
        package_name = getTest_info('test_package_name', 'package_name')
        package_atx = getTest_info('test_package_name', 'package_atx')
        if not ADB().is_install(package_name):
            ADB().install_app(package_name)
            Logging.info('install' + package_name + 'success')

        if not ADB().is_install(package_atx):
            os.system('python -m uiautomator2 init')
            Logging.info('install' + package_atx + 'success')
        else:
            pass

    @classmethod
    def afterClass(cls):
        # 返回apk主页面
        ADB().start_activity('com.verifone.adc.presentation.view.activities.MainActivity')


    def runAllCase(self):
        '''
        执行步骤:
            1:安装应用
            2:检查案例是否存在，开启driver,并且执行测试
            3:关闭driver
            4:清理logcat atx 进程

        :param driver:
        :return:
        '''
        # 解析yaml文件并执行对应操作
        Process.beforeClass()
        allyamlsList = existCase(getTest_info('test_case', 'caseYaml'))
        Page = PagePo(self.device, mkdir_file(), allyamlsList)
        Page.main()
        Process.afterClass()

    def runOneCase(self, casePath):
        '''
        执行步骤:
            1:安装应用
            2:检查案例是否存在，开启driver,并且执行测试
            3:关闭driver
            4:清理logcat atx 进程
        :param casePath:
        :return:
        '''
        Process.beforeClass()
        # driver = u2.connect(self.device)
        oneYaml = []
        oneYaml.append(casePath)
        Logging.info('当前测试用例为' + oneYaml[0])
        Page = PagePo(self.device, mkdir_file(), oneYaml)
        Page.main()
        Process.afterClass()



if __name__ == '__main__':
    pass
