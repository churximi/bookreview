#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：匹配指定中文
时间：2016年5月31日 18:31:32
"""

import re
pattern = re.compile(u'[白蓝绿黄][A-Z][A-Z0-9]{5}')
match = pattern.match(u'白A1B2C3')
if match:
    print "匹配"
else:
    print "不匹配"
