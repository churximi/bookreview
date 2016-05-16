#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：获取一个分词文本的全文列表
时间：2016年5月16日 18:39:12
"""

import codecs
import tkFileDialog


def main():
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
    f1.close()

    return wordlist

if __name__ == "__main__":
    y = main()
