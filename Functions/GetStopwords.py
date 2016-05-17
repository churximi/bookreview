#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：将停用词文本转为列表，获取停用词表
时间：2016年5月15日 22:48:24
"""

import codecs


def stopwords():
    # 打开文件
    file_path = u"D:\\GitHub\\bookreview\\Files\\停用词表.txt"    # 固定停用词表
    f1 = codecs.open(file_path, "r", encoding="utf-8")
    print u"已经打开文本：", file_path

    # 转为列表
    line_list = []
    for line in f1:
        line_list.append(line.strip())
    print u"停用词个数：", len(line_list)

    f1.close()
    return line_list

if __name__ == "__main__":
    y = stopwords()
    for item in y:
        print item
