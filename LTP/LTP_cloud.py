#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：哈工大语言云使用测试
时间：2016年4月9日 13:45:24
"""

import urllib2

url_get_base = "http://api.ltp-cloud.com/analysis/?"
api_key = 'y622c3B38TKcVPeh1wAwrVTDCbCrfqxGplrhHQ7l'  # 用户注册语言云服务后获得的认证标识

# 待分析的文本
text = "这本书实用。这本书实用还是不实用？"

format0 = 'xml'                                       # 结果格式，有xml、json、conll、plain（不可改成大写）
pattern = 'all'                                       # 指定分析模式，有ws、pos、ner、dp、sdp、srl和all

result = urllib2.urlopen("%sapi_key=%s&text=%s&format=%s&pattern=%s"
                         % (url_get_base, api_key, text, format0, pattern))
content = result.read().strip()
print content.decode("utf-8")
