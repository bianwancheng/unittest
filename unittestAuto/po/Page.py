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

import time
import os
import uiautomator2 as u2
from unittestAuto.public.LogUtils import Logging
from unittestAuto.public.PageMethod import getYaml, clickByXY, clickByText, getTest_info


class PagePo:
    def __init__(self, driver, all_result_path, yaml_list):
        self.driver = driver
        self.all_result_path = all_result_path
        self.yaml_list = yaml_list

    def analysis(self):
        pass

    def main(self):
        '''
        1、开启log
        2、执行测试
        3、记录结果
        4、存储执行结果
        5、截图
        :param driver:
        :param yaml_list:
        :return:
        '''

        operate(self.driver, self.yaml_list)


def operate(driver, yaml_list):

    driver.app_start(getTest_info('test_package_name', 'package_name'))
    Logging.success('start app success')
    # print(yaml_list)
    for yaml in yaml_list:
        caseYaml = getYaml(yaml)
        testinfo = caseYaml['testinfo']
        testcases = caseYaml['testcase']
        checks = caseYaml['check']

        for testcase in testcases:
            element_info = testcase['element_info']
            elementList = element_info.split(', ')
            # print(elementList)

            if testcase['operate_type'] == 'click':
                Logging.success(testcase['operate_type'] + testcase['info'])
                # 如果可以转换成float说明是坐标，否则就是str
                try:
                    # 可能出现异常的代码
                    elementList[0] = float(elementList[0])
                    elementList[1] = float(elementList[1])
                    clickByXY(driver, elementList)
                    time.sleep(1)
                except:
                    # 出现异常后执行的代码
                    # print('element_info内容为字符串：text='', outTime=''')
                    clickByText(driver, elementList)
                    time.sleep(1)
                else:
                    # 如果没有异常执行的代码
                    pass
                finally:
                    # 不管是否出现异常都会执行finally 具体放在那里是否可以和else一起用？
                    pass

            elif testcase['operate_type'] == 'scroll':
                Logging.success(testcase['operate_type'] + testcase['info'])
                pass

            elif testcase['operate_type'] == 'sentkey':
                Logging.success(testcase['operate_type'] + testcase['info'])
                driver(text="Settings").set_text("你好")
                pass

            else:
                Logging.warn('没有改操作请在此添加' + os.getcwd())

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


def main():
    operate()


if __name__ == '__main__':
    # 返回字典
    homeyaml = getYaml('D:\pycharm\PycharmWorkSpase\\unittestAuto\yamls\Home\home01.yaml')
    print(homeyaml)
    # print(getTest_info('test_package_name', 'package_name'))
    operate()
