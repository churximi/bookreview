#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：读入一个中文分词文本（文本是用空格分词），去除无意义词和停用词后，统计剩余词的绝对词频TF
时间：2016年5月15日 20:59:52
输出：word_tf_list，词汇与词频的列表，并按词频从大到小排序
格式：[[词1, tf1], [词2, tf2], ]
"""

import codecs
import tkFileDialog
import re
from Functions import Text2List
from Functions import Text2List_2


def getallwords():
    # 打开文件
    print u"请选择一个已经空格分好词的文本..."
    file_path = tkFileDialog.askopenfilename(title=u"选择文件")
    f1 = codecs.open(file_path, "r", encoding="utf-8")
    print u"已经打开文本：", file_path

    # 获得原始文本所有词汇
    wordlist = []
    for line in f1:
        words = line.strip().split(" ")
        for word in words:
            if word:
                wordlist.append(word)
    print u"原始文本总词数：", len(wordlist)

    # 统计词频TF，从大到小排序，去除无意义符号，去除停用词
    stopwords = Text2List_2.text2list()    # 停用词表
    word_tf_list = []
    pattern = re.compile(u'[A-Za-z\u4e00-\u9fa5]+')
    for word in set(wordlist):
        if pattern.search(word):
            if word not in stopwords:
                word_tf_list.append([word, wordlist.count(word)])
    word_tf_list.sort(key=lambda x: x[1], reverse=True)
    print u"词的种类数：", len(word_tf_list)

    f1.close()
    return word_tf_list

if __name__ == "__main__":
    list1 = getallwords()
    for item in list1:
        print item[0], "\t", item[1]

"""
更新日志
2016年5月15日 21:02:13， 为避免文本长度太大，改用对文本按行处理，而不是全部读入
"""
