#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：字典的格式化字符串测试
时间：2016年5月31日 18:55:21
"""

scores = {u"张三": u"90", u"李四": u"95", u"王五": u"80"}
print u"张三的成绩是%(张三)s" % scores
