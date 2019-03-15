#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/3/12 15:23
# @Author  :  wancheng.b
# @Site     : 
# @File     : RunAllcase.py
# @Software  : PyCharm
import os
# 检查是否有测试案例
import subprocess
import threading
import uiautomator2 as u2

from unittestAuto.po.Page import existCase, getTest_info
from unittestAuto.po.Process import Process

# 检查设备连接
def getDevices():
    '''
    换行分割截取掉头和尾，然后用\T（Tab）截取
    :return: devices_list
    '''
    devices = []
    devicesName = subprocess.getoutput('adb devices')
    devicesName = devicesName.split("\n")[1: -1]
    for deviceName in devicesName:
        deviceName = deviceName.split('\tdevice')
        devices.append(deviceName[0])
    return devices


class MyThread(threading.Thread):
    def __init__(self, device):
        super(MyThread, self).__init__()  # 重写run()方法必须要写
        self.device = device

    '''
    创建log，开启服务，加载用例
    '''

    def run(self):
        # mkdirLog()
        driver = u2.connect(self.device)
        Process().main(driver)


if __name__ == '__main__':
    if len(existCase(getTest_info('test_case', 'caseYaml'))) > 0:
        for device in getDevices():
            test_run = MyThread(device)
            test_run.start()
            test_run.join()

    else:
        print("测试案例不存在")
