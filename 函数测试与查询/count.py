#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：count()函数
时间：2016年4月18日 20:07:23
"""

import nltk

list1 = ["中文", "中文", "中", "文"]
print list1.count("中文")
print "+".join(list1[0:2])
print list1.index("中")
list1[3] = "修改"
print "+".join(list1)
