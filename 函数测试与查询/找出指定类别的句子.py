#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：从一个文本中找出指定类别的句子
时间：2016年5月20日 11:43:39
"""

import tkFileDialog
import codecs

print u"请选择一个分词文本..."
# 打开文件
file_path = tkFileDialog.askopenfilename(title=u"选择文件")
f1 = codecs.open(file_path, "r", encoding="utf-8")
print u"已经打开文本：", file_path
y = f1.readlines()
print type(y), len(y)

print u"请选择一个类别文本..."
file_path = tkFileDialog.askopenfilename(title=u"选择文件")
f2 = codecs.open(file_path, "r", encoding="utf-8")
print u"已经打开文本：", file_path
y2 = f2.readlines()

for i in range(len(y2)):
    if y2[i].strip() == "True":
        print y[i]

if __name__ == "__main__":
    pass
