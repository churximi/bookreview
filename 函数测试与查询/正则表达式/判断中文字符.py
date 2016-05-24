#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：判断字符串中是否含有中文
时间：2016年4月30日 16:28:12
"""

import re

zhPattern = re.compile(u'[\u4e00-\u9fa5]+')    # 包括繁体中文
content1 = u"繁體123"
match1 = zhPattern.search(content1)

if match1:
    print u"含有中文"
else:
    print u"不含中文"
