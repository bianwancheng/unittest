#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/3/12 14:43
# @Author  :  wancheng.b
# @Site     : 
# @File     : TestSuit.py
# @Software  : PyCharm

# 构造测试集
import os
import unittest

case_path = os.getcwd()  # case所在路径
discover = unittest.defaultTestLoader.discover(case_path, pattern="*Test.py")
# print(discover)
# discover相当于在指定的case所在的路径里寻找所有名称模式匹配pattern的文件并加载其内容，相当于suite的集合
runner = unittest.TextTestRunner(verbosity=2)  # verbosity控制输出的执行结果的详细程度，可为0，1，2，其中0最简单，1是默认值，2最详细
runner.run(discover)
