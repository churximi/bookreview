#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：获取Html网页的源码内容
输入：需要爬取的网页URL
返回：网页源码
时间：2016年5月14日 22:11:01
"""

import urllib2


def gethtml(url):    # 参数为网址
    headers = {'User-Agent': 'Mozilla/4.0 (Windows NT 6.0) AppleWebKit/535.11 '
                             '(KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'}
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request, timeout=5)    # 超时设置
    content = response.read().decode('utf-8')

    return content

if __name__ == "__main__":
    print u"测试", gethtml("http://im.nju.edu.cn/")

"""
对付反爬虫措施：
1.考虑代理
2.更改headers
3.设置爬取间隔，例如随机时间0~5秒
"""