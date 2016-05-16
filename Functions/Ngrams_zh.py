#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：针对中文的ngram()函数，输入某个中文分词列表和数值n，执行ngram()并按词频从大到小排序
返回：返回一个列表，列表中是多个[新词， 词频]
例如：分词列表 ["信息", "检索", "信息", "组织"]
时间：2016年4月25日 19:44:05
"""

import nltk


def ngram(par_list, par_n):
    temp = nltk.ngrams(par_list, par_n)      # n-gram
    newwords_list = []
    for item in temp:
        newwords_list.append("".join(item))          # 组合后的新词

    new = []
    for newword in set(newwords_list):
        new.append([newword, str(newwords_list.count(newword))])   # 存储新词和词频
    new.sort(key=lambda x: int(x[1]), reverse=True)        # 按词频大小排序

    return new

if __name__ == "__main__":
    list1 = ["信息", "检索", "信息", "检索"]
    y = ngram(list1, 2)
    for xx in y:
        print xx[0], xx[1]
