#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：获取某个目录下的文件名和目录名（下级目录）
时间：2016年4月30日 16:11:37
"""

import os

filenames = os.listdir(raw_input(u"请输入路径："))
for item in filenames:
    print item
