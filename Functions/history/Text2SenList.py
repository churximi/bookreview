#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：获取文本中句子的词汇列表
参数：文本路径
返回：所有句子的列表，每个句子元素又是一个词汇的列表
时间：2016年5月2日 14:16:25
"""

import codecs
import tkFileDialog


def main():
    # 打开文件
    file_path = tkFileDialog.askopenfilename(title=u"选择文件")
    f1 = codecs.open(file_path, "r", encoding="utf-8")
    print u"已经打开文本：", file_path

    # 获得句子列表，其中每个句子又是词汇的列表
    sentences_list = []
    for line in f1:
        single_sen_list = line.strip().split(" ")
        while "" in single_sen_list:
            single_sen_list.remove("")
        sentences_list.append(single_sen_list)
    print u"句子总数：", len(sentences_list)

    f1.close()
    return sentences_list

if __name__ == "__main__":
    y = main()

"""
更新日志
2016年5月7日 00:27:06，添加窗口选择功能
2016年5月17日 20:17:20， 已加入TextSta类

"""