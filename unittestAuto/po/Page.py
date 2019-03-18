#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/3/13 17:01
# @Author  :  wancheng.b
# @Site     : 
# @File     : Page.py
# @Software  : PyCharm
import configparser
import time

import yaml
import os
import uiautomator2 as u2

# # 检查测试案例是否存在,return casedirlist
# def existCase(path):
#     caseList = []
#     for dirpath, dirname, files in os.walk(path):
#         for file in files:
#             # print(os.path.join(dirpath, file))
#             caseList.append(os.path.join(dirpath, file))
#     print('测试案例共有' + str(len(caseList)))
#     return caseList
#
# '''
# 获取test_info.ini section下面的key对应的value值
# '''
#
#
# def getTest_info(section, key):
#     config = configparser.ConfigParser()
#     config.read('H:\homeGit\\unittest\\unittestAuto\data\\test_info.ini', encoding='utf-8')
#     return config.get(section, key)
#
#
# '''
# 解析yaml，return：dict
# '''
#
#
# def getYaml(path):
#     with open(path, 'r', encoding='utf-8')as f:
#         deviceYaml = yaml.load(f)
#     return deviceYaml
from unittestAuto.public.PageMethod import getYaml, clickByXY, clickByText


def operate(driver, yaml_list):
    driver.app_start('com.verifone.scb.presentation')
    print(yaml_list)
    for yaml in yaml_list:
        print(12313123)
        caseYaml = getYaml(yaml)
        testinfo = caseYaml['testinfo']
        testcases = caseYaml['testcase']
        checks = caseYaml['check']

        for testcase in testcases:
            element_info = testcase['element_info']
            elementList = element_info.split(',')

            if testcase['operate_type'] == 'click':
                print(testcase['operate_type'] + testcase['info'])
                # 如果第一个为float类型选择clickByXY()方法
                if type(elementList[0]) == float:
                    clickByXY(driver, element_info)
                else:
                    clickByText(driver, element_info)
                time.sleep(1)
                # d(test='').click(timeout=10)

            elif testcase['operate_type'] == 'scroll':
                print(testcase['operate_type'] + testcase['info'])
                pass

            elif testcase['operate_type'] == 'sentkey':
                print(testcase['operate_type'] + testcase['info'])
                driver(text="Settings").set_text("你好")
                pass

            else:
                print('没有改操作请在此添加' + os.getcwd())

        for check in checks:
            pass
            # 可以研究下具体有什么检查方式
            # if check['operate_type'] == 'click':
            #     print(check['operate_type'] + check['info'])
            #     d(test='').click()
            # if check['operate_type'] == 'scroll':
            #     print(check['operate_type'] + check['info'])
            #     pass
            # if check['operate_type'] == 'sentkey':
            #     print(check['operate_type'] + check['info'])
            #     pass
            # else:
            #     print('没有改操作请在此添加' + os.getcwd())


if __name__ == '__main__':
    # 返回字典
    homeyaml = getYaml('D:\pycharm\PycharmWorkSpase\\unittestAuto\yamls\Home\home01.yaml')
    print(homeyaml)
    # print(getTest_info('test_package_name', 'package_name'))
    operate()
