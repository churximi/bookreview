#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：字典dic
时间：2016年5月31日 19:12:06
"""

scores = {u"张三": u"90", u"李四": u"95", u"王五": u"80"}
for item in scores:
    x, y = item, scores[item]
    print x, y
