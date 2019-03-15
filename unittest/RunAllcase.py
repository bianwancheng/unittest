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
import unittest
from po.Page import getTest_info

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
        # driver = u2.connect(self.device)
        case_path = getTest_info('test_case', 'case')  # case所在路径
        print(case_path)
        discover = unittest.defaultTestLoader.discover(case_path, pattern="Process.py")
        runner = unittest.TextTestRunner(verbosity=2)  # verbosity控制输出的执行结果的详细程度，可为0，1，2，其中0最简单，1是默认值，2最详细
        runner.run(discover)

if __name__ == '__main__':
    # print(existCase("D:\pycharm\PycharmWorkSpase\\unittest\yamls"))
    for device in getDevices():
        test_run = MyThread(device)
        test_run.start()
        test_run.join()
