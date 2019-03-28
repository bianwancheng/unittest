# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     RunOneCase.py
   Description :
   Author :       bianwancheng
   date：          2019/3/18
-------------------------------------------------
   Change Activity:
                   2019/3/18:
-------------------------------------------------
__author__ = 'wancheng.b'
"""

# 检查是否有测试案例
import subprocess
import threading
from unittestAuto.po.Process import Process
from unittestAuto.public.LogUtils import Logging
from unittestAuto.public import LogUtils as U
from unittestAuto.public.PageMethod import getTest_info, existCase


@U.l()
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
    if len(devices) > 0:
        return devices
    else:
        Logging.warn('设备未连接')


class MyThread(threading.Thread):
    def __init__(self, device):
        super(MyThread, self).__init__()  # 重写run()方法必须要写
        self.device = device


    def run(self):
        Process(self.device).runAllCase()


if __name__ == '__main__':
    if len(existCase(getTest_info('test_case', 'caseYaml'))) > 0:
        for device in getDevices():
            test_run = MyThread(device)
            test_run.start()
            test_run.join()

    else:
        Logging.error("测试案例不存在")
