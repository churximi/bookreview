# -*- coding:utf-8 -*-

"""
功能：python跳出循环
"""
# 方法2：封装为函数，return


def test():
    for i in range(5):
        for j in range(5):
            if i == j == 2:
                return
            else:
                print i, '----', j

test()
