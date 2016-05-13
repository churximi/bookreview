#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：测试__name__ == '__main__'的作用
时间：2016年5月13日 23:03:46
"""


def _test1():
    print "Hello, world!"


def _test2():
    print "Hi, world!"


def test(x):
    if x > 5:
        return _test1()
    else:
        return _test2()

if __name__ == '__main__':
    test(5)
    print u"测试"
