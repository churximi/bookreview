#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：删除亚马逊图书网页源码中的注释，注释规则：<!--    -->
时间：2016年5月11日 23:03:54
"""

import re
from Functions import GetHtml

# 获取网页源码内容
url = ("https://www.amazon.cn/s/ref=sr_pg_2?" +
       "rh=n%3A658390051%2Cn%3A%21658391051%2Cn%3A658414051%2Cp_6%3AA1AJ19PSB66TGU&page=1")
content = GetHtml.gethtml(url)
print u"解析网址：", url

# 删除注释
pat1 = re.compile(u"<!--.*?-->", re.S)
content = pat1.sub("", content)

# 获取图书编码，每页16个
pat2 = re.compile('data-asin="(.*?)" class=.*?result', re.S)
bookcodes = re.findall(pat2, content)
print u"图书编码个数：", len(bookcodes)
print "\n".join(bookcodes)
print u"程序结束！"
