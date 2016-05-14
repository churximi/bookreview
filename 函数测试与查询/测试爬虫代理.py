#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：测试爬虫代理
时间：2016年5月14日 22:41:49
"""

from Functions import GetHtml
from Functions import GetProxyIPs
from Functions import UseProxy

print u"正在获取代理IP列表..."
ips = GetProxyIPs.getips()

UseProxy.proxy(ips[0])
print u"启用代理ip：", ips[0]

content = GetHtml.gethtml("https://www.baidu.com/")
print u"获取网页内容：", content
