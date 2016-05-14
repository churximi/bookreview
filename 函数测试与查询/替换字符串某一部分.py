#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：替换字符串指定的某部分内容
时间：2016年5月15日 01:28:37
"""

import re

text = "https://www.amazon.cn/s/ref=658414051&ie=UTF8&qid=1463245898&rnid=658414051"
pat = re.compile(u"(.*?)ie=UTF8", re.S)
content = pat.findall(text)
print content[0] + "page="
