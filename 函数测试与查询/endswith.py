#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：读取文件
时间：2016年4月17日 13:18:29
"""

f = open(r"file\test.txt")
for line in f:
    if line.strip().endswith("jpg"):    # 读取文件某一行的时候，是会包括行末符号的（看不见的换行符等）
        print line.strip()
