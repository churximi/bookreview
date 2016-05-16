#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：爬虫的基本框架
时间：2016年5月16日 20:21:33
"""

from Functions import GetHtml
import re

content = GetHtml.gethtml("http://im.nju.edu.cn/")    # 获取网页源码
pattern = re.compile(r"head>.*?title>(.*?)</title>", re.S)    # 正则表达式
finds = pattern.findall(content)
for item in finds:
    print u"爬取的内容：", item

print u"程序结束！"

if __name__ == "__main__":
    pass
