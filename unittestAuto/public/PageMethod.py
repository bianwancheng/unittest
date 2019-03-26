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

# 检查测试案例是否存在,return casedirlist
import configparser
import os

import yaml

'''
测试案例是否存在return caseDirList
'''


def existCase(path):
    caseList = []
    for dirpath, dirname, files in os.walk(path):
        for file in files:
            # print(os.path.join(dirpath, file))
            caseList.append(os.path.join(dirpath, file))
    print('测试案例共有' + str(len(caseList)))
    return caseList


'''
获取test_info.ini section下面的key对应的value值
'''


def getTest_info(section, key):
    config = configparser.ConfigParser()
    config.read('D:\pycharm\PycharmWorkSpase\\unittest\\unittestAuto\data\\test_info.ini', encoding='utf-8')
    return config.get(section, key)


'''
解析yaml，return：dict
'''


def getYaml(path):
    with open(path, 'r', encoding='utf-8')as f:
        deviceYaml = yaml.load(f)
    return deviceYaml


'''
@ description 通过X, Y 坐标点击
@:parameter driver, elementinfo_List

'''


def clickByXY(driver, elementList):
    driver.click(elementList[0], elementList[1])


'''
@description 通过text点击
@:parameter driver, elementinfo_List
'''


def clickByText(driver, elementList):
    driver(text=elementList[0]).click(timeout=int(elementList[1]))
