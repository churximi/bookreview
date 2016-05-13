#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：readlines()读入文本
时间：2016年5月13日 22:45:20
"""

with open(r"test.txt", "r") as f1:    # 读入文本
    lines_list = f1.readlines()

print u"文本行数：", len(lines_list)

"""
备注：
1.readlines()得到的是一个list，一次读入内存，列表元素会含有换行符
2.空行也会读入，作为列表的一个元素
3.用with open打开一个文本，操作结束后会自动close
"""
