#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：将特征词及其DF统计的文本转化为列表
输入：选择文本，文本中存放的是特征词及其DF统计，格式：每行一个，特征词和DF数据之间用制表符\t分隔
返回：特征词dic词典，key为特征词，key值为特征词的DF值
时间：2016年5月2日 14:16:25
"""

import codecs
import tkFileDialog
import re


def getfilewords():
    pat = re.compile(u"[A-Za-z\u4e00-\u9fa5]+")
    words_dic = {}    # 存放特征词及其DF值
    words_list = []    # 单独存放特征词，保证顺序
    print u"请选择特征词文件..."  # 通过文件对话窗口选择文件，返回数据库路径
    f1 = codecs.open(tkFileDialog.askopenfilename(title=u"选择文件"), "r", encoding="utf-8")
    for line in f1:
        temp = line.strip().split("\t")
        if pat.search(temp[0]):           # 含有中文和英文字符的特征词，才留下
            words_dic[temp[0]] = temp[1]
            words_list.append(temp[0])    # 以原来的顺序存储特征词

    f1.close()
    return words_dic, words_list

if __name__ == "__main__":
    y = getfilewords()
    dic_test, list_test = y[0], y[1]    # 测试代码，分别获取列表和词典
    print len(dic_test), len(list_test)
    for item in list_test:
        print item
    for item in list_test:
        print item, dic_test[item]


"""
更新日志
2016年5月6日 17:23:55，通过窗口选择文件
2016年5月6日 17:43:33，可以直接通过一个特征词及DF统计的文件，存储特征词及DF值，不再需要分别读两个文件
2016年5月6日 18:06:15，加入筛选特征词的功能

"""