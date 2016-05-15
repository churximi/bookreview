#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：查询一个列表的是否有重复的元素
时间：2016年5月15日 21:53:59
"""

import tkFileDialog
import codecs

file_path = tkFileDialog.askopenfilename(title=u"选择文件")
f1 = codecs.open(file_path, "r", encoding="utf-8")
print u"已经打开文本：", file_path

file_list = []
for line in f1:
    file_list.append(line.strip())
for item in file_list:
    if file_list.count(item) > 1:
        print u"存在重复的元素：", item
