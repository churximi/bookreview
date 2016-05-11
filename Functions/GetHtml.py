#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：给定网址，获取Html网页的源码内容
时间：2016年5月11日 23:22:37
"""

import urllib2


def gethtml(url):    # 参数为网址
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) '
                             'Chrome/17.0.963.12 Safari/535.11'}
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')

    return content
