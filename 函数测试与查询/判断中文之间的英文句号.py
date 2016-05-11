#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：判断中文之间的英文句号（含多个），两个中文之间的英文句号会被更换为中文句号
时间：2016年4月11日 19:39:54
"""

import re

dot_pat = re.compile(u'[\u4e00-\u9fa5][.]+[\u4e00-\u9fa5]')    # 检测中文之间的英文句号
content = u'中文.中国..中央......但这个1.不替换'
finds = re.findall(dot_pat, content)
for find in finds:
    temp = find.replace(".", u"。")    # 把.替换为。
    content = content.replace(find, temp)
print content
