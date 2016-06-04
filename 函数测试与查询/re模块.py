#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：学习re模块
时间：2016年6月1日 18:31:01
"""

import re

# re.match
text = u"这是一个测试句。这是第二个测试句。这是第三个测试句。"
a = re.match(u"这是", text)
print u"match " + a.group(0) if a else u"not match"

# re.search
b = re.search(u"一个", text)
print u"search " + b.group(0) if b else u"not search"

# re.sub
c = re.sub(u"测试", u"【测试】", text)
d = re.sub(u"测试", u"【测试】", text, count=1)  # 替换一个
print c, "\n", d

# re.split
e = re.split(u"。", text)
print "\n".join(e)
f = re.split(u"(。)", text)  # 加括号表示保留
print "\n".join(f)

# re.findall
g = re.findall(u"[\u4e00-\u9fa5]+。", text)
print "\n".join(g)
