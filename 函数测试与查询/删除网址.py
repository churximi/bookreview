#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：删除文本里的网址，正则表达式练习
时间：2016年4月11日 14:13:00
"""

import re

text = u"这是网址：https://www.baidu.com/。http://www.baidu.com/"
print u"原始文本：", text
pattern = re.compile("http[s]*:[/.?%&=\-\w]*", re.S)    # 删除网址
text = pattern.sub("", text)    # re.sub函数进行以正则表达式为基础的替换工作
print u"处理完毕：", text
