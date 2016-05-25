# -*- coding:utf-8 -*-

"""
功能：python跳出循环
"""
# 方法1：自定义异常


class Getoutofloop(Exception):
    pass
try:
    for i in range(5):
        for j in range(5):
            if i == j == 2:
                raise Getoutofloop()
            else:
                print i, '----', j
except Getoutofloop:
    pass
