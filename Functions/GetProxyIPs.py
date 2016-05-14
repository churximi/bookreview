# -*- coding:utf-8 -*-

"""
功能：从www.xicidaili.com获取免费代理IP
输入：无
返回：代理ip列表
版本：2016年5月14日 22:26:13
"""

import re
from Functions import GetHtml


def getips():
    proxy_ips = []
    content = GetHtml.gethtml("http://www.xicidaili.com/nn")    # 获取网页源码
    pattern = re.compile('<tr.*?<img.*?</td.*?<td>(.*?)</td>.*?<td>(.*?)</td>', re.S)
    items = re.findall(pattern, content)
    for item in items:
        proxy_ips.append(item[0] + ":" + item[1])
    print u"已获取代理ip个数：", len(proxy_ips)

    return proxy_ips

if __name__ == "__main__":
    ips = getips()
    print ips[0]
