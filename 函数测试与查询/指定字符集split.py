#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：用指定的字符集分割句子
时间：2016年4月11日 16:59:09
"""

import re

pat = re.compile(u"[。？！；]|[…]{2}")        # 用五种标点分句
text = u"句子1。句子2；句子3……句子4！句子5？"
text_list = re.split(pat, text)    # 分割的最后一个元素为空元素
for x in text_list:
    if x:
        print x
print u"----------"

# 如果想要保留分割符，用（）括起来
pat2 = re.compile(u"([。？！；]|[…]{2})")
text_list2 = re.split(pat2, text)
for x in text_list2:
    if x:
        print x
print u"----------"

# 如果想要保留句子的标点
punctuation_list = [u"。", u"？", u"！", u"；", u"……"]
text2 = text
for punctuation in punctuation_list:
    text2 = text2.replace(punctuation, punctuation + u" ")    # 用空格分割
print text2
text_list3 = re.split(u" ", text2)
for x in text_list3:
    if x:
        print x
print u"----------\n程序结束！"
