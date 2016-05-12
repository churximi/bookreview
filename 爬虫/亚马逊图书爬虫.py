#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：爬取亚马逊图书，给定某类图书的网址，获取图书书评内容
时间：2016年5月11日 23:53:51
"""

import codecs
from Functions import GetHtml
import re
import time
import urllib2


def proxy(ipnum):
    enable_proxy = False
    if enable_proxy:
        proxy_yes = urllib2.ProxyHandler({"http": IP[ipnum]})
        opener = urllib2.build_opener(proxy_yes)
        urllib2.install_opener(opener)
    return


def getreviews(page1, ip_num):
    for i in range(page1, len(allbookcodes)):
        pagenum = 1
        while pagenum < 2000:
            review_url = ("http://www.amazon.cn/product-reviews/" + allbookcodes[i] +
                          "/ref=cm_cr_pr_viewopt_srt?ie=UTF8&showViewpoints=1&sortBy=helpful" +
                          "&pageNumber=" + str(pagenum))
            print u"正在爬取网址：", review_url
            try:
                content = GetHtml.gethtml(review_url)  # 获取书评网页源码
                # 某一页上的所有书评内容
                pat0 = re.compile(r'ReviewCount">(.*?)</span>')
                reviews_num = re.findall(pat0, content)
                print u"书评数量：", reviews_num[0]

                pat1 = re.compile(r'review-text">(.*?)</span>')
                reviews = re.findall(pat1, content)

                pat2 = re.compile(r'<[^>]+>', re.S)  # 用于去除内容里的html标签
                if (pagenum-1)*10 < int(reviews_num[0]):
                    if len(reviews) > 0:  # 判断本页是否有书评内容
                        for j in range(len(reviews)):
                            review = pat2.sub("", reviews[j])
                            f.write(review + "\n")
                    elif len(reviews) == 0:
                        print u"此页需要重新爬取..."
                        time.sleep(1)
                        pagenum -= 1
                        continue
                    pagenum += 1
                else:
                    break  # 跳出当前书的循环，进入下一本书
            except:
                print u"出现异常，准备重启...\n\n"
                if ip_num > 95:
                    ip_num = 0
                ip_num += 1
                proxy(ip_num)
                print u"切换代理：", IP[ip_num]
                time.sleep(1)
                continue

# 获取代理IP
IP = []
cont = GetHtml.gethtml("http://www.xicidaili.com/nn")
pattern = re.compile('<tr.*?<img.*?</td.*?<td>(.*?)</td>.*?<td>(.*?)</td>', re.S)
items = re.findall(pattern, cont)
for item in items:
    IP.append(item[0] + ":" + item[1])
print u"IP代理个数：", len(IP)

proxy(1)

# 读取图书唯一编码列表
allbookcodes = []
with open("allbookcodes.txt", "r") as f:
    for line in f:
        code = line.strip()
        if code not in allbookcodes:    # 去重
            allbookcodes.append(code)
print u"图书编码个数（即图书本数）：", len(allbookcodes)

# 写入文本
f = codecs.open("allbooks.xml", "a", "utf-8")
f.truncate()

getreviews(948, 0)

f.close()
print(u"\n程序结束！")
