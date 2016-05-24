#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：判断字符串中是否含有有效字符（中文、英文、数字、下划线）
时间：2016年4月30日 17:53:41
"""

import re

zhPattern = re.compile(u'[\w\u4e00-\u9fa5]+')
content1 = u'中文，。？！……-+#'
match1 = zhPattern.search(content1)

if match1:
    print u"含有有效字符"
else:
    print u'不含有效字符'