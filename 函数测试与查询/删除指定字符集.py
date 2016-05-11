#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：删除指定字符集中的字符
时间：2016年4月11日 20:45:06
"""

import re

spec_pat = re.compile(u'[‘’<>“”*★]')
text = u"这<是>一个“测试”文‘本’**★。"
text = spec_pat.sub("", text)
print text
