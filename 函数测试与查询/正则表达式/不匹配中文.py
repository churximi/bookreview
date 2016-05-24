#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：不匹配文字，只匹配英文数字符号等
时间：2016年5月21日 21:08:42
"""

import re

text = u"你好    你.好    你-好    你*好    你 好    你\t好    你们好    你真好    你不好"
pat = re.compile(u"你[^\u4e00-\u9fa5]+好")
finds = pat.findall(text)
for find in finds:
    print find

if __name__ == "__main__":
    pass
