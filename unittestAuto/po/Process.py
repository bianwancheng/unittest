#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/3/13 16:12
# @Author  :  wancheng.b
# @Site     : 
# @File     : Process.py
# @Software  : PyCharm
# import unittestAuto
import os
import random
import time
import uiautomator2 as u2
from unittestAuto.lib.adbUtils import ADB
from unittestAuto.po.Page import operate, PagePo
from unittestAuto.public.GetLog import Al
from unittestAuto.public.LogUtils import Logging
from unittestAuto.public.PageMethod import getTest_info, existCase


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

    @classmethod
    def __save_android_log(self):
        """

        :return:清理当前设备缓存log,并且记录当前设备log
        """
        android_log = Al(self.device)
        log_file = self.all_result_path + '/log/{}.log'.format(self.filename)
        android_log.main(log_file)
        return log_file

    @classmethod
    def __save_android_result(self):
        """
        生成测试报告
        :return: 测试报告路径
        """
        r = Gr(self.all_result_path, self.device)
        r.main()
        return self.all_result_path

    @classmethod
    def mkdir_file(self):
        """

        :return:创建日志存放文件夹
        """
        result_file = getTest_info('test_case', 'log_file')
        result_file_every = result_file + '/' + \
                            time.strftime("%Y-%m-%d_%H_%M_%S{}".format(random.randint(10, 99)),
                                          time.localtime(time.time()))
        file_list = [
            result_file,
            result_file_every,
            result_file_every + '/log',
            result_file_every + '/per',
            result_file_every + '/img',
            result_file_every + '/status']
        if not os.path.exists(result_file):
            os.mkdir(result_file)

        for file_path in file_list:
            if not os.path.exists(file_path):
                os.mkdir(file_path)
        return result_file_every

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
        driver = u2.connect(self.device)
        operate(driver, allyamlsList)
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
        driver = u2.connect(self.device)
        oneYaml = []
        oneYaml.append(casePath)
        Logging.info('当前测试用例为' + oneYaml[0])
        Page = PagePo(driver, self.mkdir_file(), oneYaml)
        Page.main()
        Process.afterClass()


if __name__ == '__main__':
    pass
