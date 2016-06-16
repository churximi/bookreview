#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：连接路径名
时间：2016年5月4日 15:02:47
"""

import os

path1 = r"C:\Users\lenovo\Desktop\test0504"
filename = u"中文sentences.accdb"
print os.path.join(path1, filename)
