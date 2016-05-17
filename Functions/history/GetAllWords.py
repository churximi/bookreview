#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：读入一个中文分词文本（文本是用空格分词），去除无意义词和停用词后，统计剩余词的绝对词频TF
时间：2016年5月15日 20:59:52
输出：word_tf_list，词汇与词频的列表，并按词频从大到小排序
格式：[[词1, tf1], [词2, tf2], ]
"""

import re

from Functions import GetStopwords
from Functions.history import GetTextList


def main():
    wordlist = GetTextList.main()    # 获取全文词汇列表

    # 统计词频TF，从大到小排序，去除无意义符号，去除停用词
    stopwords = GetStopwords.stopwords()    # 停用词表
    word_tf_list = []
    pattern = re.compile(u'[A-Za-z\u4e00-\u9fa5]+')
    for word in set(wordlist):
        if pattern.search(word):
            if word not in stopwords:
                word_tf_list.append([word, wordlist.count(word)])
    word_tf_list.sort(key=lambda x: x[1], reverse=True)
    print u"词的种类数：", len(word_tf_list)

    return word_tf_list

if __name__ == "__main__":
    list1 = main()
    for item in list1:
        print item[0], "\t", item[1]

"""
更新日志
2016年5月15日 21:02:13， 为避免文本长度太大，改用对文本按行处理，而不是全部读入
2016年5月16日 18:47:07， 将部分代码模块化
2016年5月17日 19:51:25， 已加入类TextSta中
"""
