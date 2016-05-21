#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：测试NLTK的ngrams()，针对中文实验
时间：2016年4月25日 19:28:48
"""

import nltk

list1 = ["信息", "检索", "信息", "组织", "信息", "咨询", "信息", "检索", "信息"]    # 测试列表

temp = nltk.ngrams(list1, 2)          # 2-gram，也可以用nltk.bigrams
list2 = []
for item in temp:
    list2.append("".join(item))       # 两两组合后的新词

list3 = []
for newword in set(list2):
    list3.append([newword, str(list2.count(newword))])    # 存储新词和词频
list3.sort(key=lambda x: int(x[1]), reverse=True)         # 按词频大小排序

for item in list3:
    print "".join(item)
