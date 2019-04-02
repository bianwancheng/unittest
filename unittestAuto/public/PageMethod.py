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
import random
import time
import yaml
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


def mkdir_file():
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
        result_file_every + '/html',
        result_file_every + '/img',
        # result_file_every + '/status'
    ]
    if not os.path.exists(result_file):
        os.mkdir(result_file)

    for file_path in file_list:
        if not os.path.exists(file_path):
            os.mkdir(file_path)
    return result_file_every
