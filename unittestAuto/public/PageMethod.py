# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     PageMethod
   Description :
   Author :       bianwancheng
   date：          2019/3/18
-------------------------------------------------
   Change Activity:
                   2019/3/18:
-------------------------------------------------
__author__ = 'wancheng.b'
"""

import configparser
import os
import yaml
from unittestAuto.public import LogUtils as U
from unittestAuto.public import LogUtils
from unittestAuto.public.LogUtils import Logging

'''
测试案例是否存在return caseDirList
'''


def existCase(path):
    if os.path.exists(path):
        caseList = []
        for dirpath, dirname, files in os.walk(path):
            for file in files:
                # print(os.path.join(dirpath, file))
                caseList.append(os.path.join(dirpath, file))
        Logging.info('测试案例共有' + str(len(caseList)) + '个，' + '用例路径：' + path)
        return caseList
    else:
        Logging.error('测试案例路径不存在')


'''
获取test_info.ini section下面的key对应的value值
'''


def getTest_info(section, key):
    try:
        config = configparser.ConfigParser()
        config.read('D:\pycharm\PycharmWorkSpase\\unittest\\unittestAuto\data\\test_info.ini', encoding='utf-8')
        return config.get(section, key)
    except Exception as e:
        Logging.error('test_info.ini路径错误:{}'.format(e))
        raise e


'''
解析yaml，return：dict
'''


@LogUtils.l()
def getYaml(path):
    with open(path, 'r', encoding='utf-8')as f:
        deviceYaml = yaml.load(f)
    return deviceYaml


'''
@ description 通过X, Y 坐标点击
@:parameter driver, elementinfo_List

'''


def clickByXY(driver, elementList):
    try:
        driver.click(elementList[0], elementList[1])
        Logging.success('driver click' + elementList[0] + 'success by XY')
    except Exception as e:
        raise e


'''
@description 通过text点击
@:parameter driver, elementinfo_List
'''


def clickByText(driver, elementList):
    try:
        driver(text=elementList[0]).click(timeout=int(elementList[1]))
        Logging.success('driver click' + elementList[0] + 'success by Text')
    except Exception as e:
        raise e


@U.l()
def __save_android_log(self):
    """

    :return:清理当前设备缓存log,并且记录当前设备log
    """
    android_log = public.GetLog.Al(self.device)
    log_file = self.all_result_path + '/log/{}.log'.format(self.filename)
    android_log.main(log_file)
    return log_file
