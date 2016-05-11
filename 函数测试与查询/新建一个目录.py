#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：新建一个文件夹
时间：2016年4月11日 14:41:48
"""

import os

newfolder = raw_input(u"请输入要新建的文件夹路径：")
if not os.path.exists(newfolder):    # 判断文件夹是否存在
    os.mkdir(newfolder)
    print u"已经新建了一个文件夹。"
else:
    print u"文件夹已经存在"

print u"程序结束！"
