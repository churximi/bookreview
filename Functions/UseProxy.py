#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：启用爬虫代理，以解决爬取过程中本地ip被禁止的问题
输入：代理ip及端口，例如61.135.217.15:80
返回：无，将启用ip代理功能
时间：2016年5月14日 22:32:12
"""

import urllib2


def proxy(ip):
    if ip:
        proxy_yes = urllib2.ProxyHandler({"http": ip})
        opener = urllib2.build_opener(proxy_yes)
        urllib2.install_opener(opener)

    return

if __name__ == "__main__":
    pass
