#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：爬取亚马逊图书，给定某类图书的网址，获取图书编码，为爬取图书信息做准备
例如：计算机与互联网类
时间：2016年5月15日 02:57:37
"""

from Functions import GetHtml
import re
import codecs
import time
from Functions import UseProxy
from Functions import GetProxyIPs
import random


def getcodes():
    # 启用代理
    ip_num = 0
    ips = GetProxyIPs.getips()
    UseProxy.proxy(ips[ip_num])

    pat0 = re.compile(u"(.*?)page=", re.S)
    url_01 = raw_input(u"请输入某类别亚马逊图书某一页网址:\n" +
                       u"网址最后的形式应为：&page=xx&ie=UTF8&qid=yy\n")
    pagenum = raw_input(u"请输入要爬取的图书页数（每页16本）：")

    # 主程序
    allbookcodes = []
    i = 1
    while i <= int(pagenum):
        url_02 = pat0.findall(url_01)    # 抽取网址其中一部分
        url = url_02[0] + "page=" + str(i)  # 初始网址组合
        print u"★★★正在爬取第" + str(i) + u"页的图书..."
        print u"当前爬取网页：", url

        try:
            content = GetHtml.gethtml(url)
            time.sleep(5 * random.random())    # 随机休息0~5秒
            pat1 = re.compile(u"<!--.*?-->", re.S)
            content = pat1.sub("", content)    # 删除源码注释部分，去除干扰

            pat2 = re.compile('data-asin="(.*?)" class=.*?result', re.S)
            bookcodes = re.findall(pat2, content)    # 图书编号，每页16个，这是一个list
            i += 1

            if len(bookcodes) == 0:    # 如果没爬到网页
                print u"当前网页未抓取到，准备重抓..."
                time.sleep(5)
                i -= 1
                continue
            allbookcodes += bookcodes

        except:
            print u"出现异常，准备重启...\n\n"
            ip_num += 1
            if ip_num == len(ips):
                print u"★★★警告：代理ip列表已经用完，将重新遍历使用..."
                ip_num = 0
            UseProxy.proxy(ips[ip_num])
            print u"网络异常，准备切换代理：", ips[ip_num]
            time.sleep(1)
            continue

    print u"图书编码总个数：", len(set(allbookcodes))
    return list(set(allbookcodes))

if __name__ == "__main__":
    codeslist = getcodes()
    f = codecs.open("allbookcodes.txt", "a", "utf-8")
    for bookcode in codeslist:
        f.write(bookcode + "\n")
