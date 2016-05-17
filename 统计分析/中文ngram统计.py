#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：统计中文的ngram词汇（常用2-gram），进而优化分词问题和词频统计问题
输入：词汇list，2
返回：2-gram新词，以及找出新词里原有的词（与组合前的词汇对比）
时间：2016年5月16日 20:13:27
例如：【初学者】可能会被分词为【初】【学者】，而【学者】本身是一个不同的词
"""

import codecs
import re

from Functions import Ngrams_zh
from Functions.history import GetTextList

wordlist = GetTextList.main()    # 获取文本的全文词汇列表
newlist = Ngrams_zh.ngram(wordlist, 2)    # 2-gram处理，获得新词

# 存放新词
f1 = codecs.open(u"2_gram新词.txt", "a", "utf-8")
f1.truncate()
f2 = codecs.open(u"2_gram里的旧词.txt", "a", "utf-8")
f2.truncate()

pat = re.compile(u'[《》，。？！…、:：（）；;()~]')    # 一些特殊符号
for item in newlist:
    if not pat.search(item[0]):    # 不含符号的组合，比如不能跨标点组合新词
        text = "\t".join(item)    # 连接新词和词频
        f1.write(text + "\n")
        if item[0] in wordlist:
            f2.write(text + "\n")

f1.close()
f2.close()

print u"程序结束！"
