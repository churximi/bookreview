#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：比较两个字符串的相似度，difflib.SequenceMatcher
时间：2016年5月13日 23:10:39
"""

from difflib import SequenceMatcher as Sim

a = "a"
b = "ab"
c = "abc"

print u"a与a的相似度：", Sim(None, a, a).ratio()
print u"a与b的相似度：", Sim(None, a, b).ratio()
print u"a与c的相似度：", Sim(None, a, c).ratio()
print u"b与a的相似度：", Sim(None, b, c).ratio()

"""
备注：
计算原理，大体是=两者相同的部分长度和/两者总体长度
"""