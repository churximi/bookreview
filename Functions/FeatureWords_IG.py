#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：获取指定数量的特征词列表、字典
输入：信息增益特征词列表
时间：2016年5月19日 19:10:41
"""

import codecs
import tkFileDialog
from Functions.TextSta import TextSta


def main(word_df):
    # 打开文件
    file_path = u"D:\\GitHub\\bookreview\\Files\\信息增益特征词排序.txt"    # 信息增益特征词列表
    f1 = codecs.open(file_path, "r", encoding="utf-8")
    print u"已经打开文本：", file_path

    # 转为列表
    line_list = []
    for line in f1:
        line_list.append(line.strip())
    f1.close()

    fw_num = raw_input(u"请输入要选择的特征词个数...\n")
    fw_list = line_list[:int(fw_num)]    # 获取指定数量的特征词

    fw_dic = {}    # 存储特征词及其DF值
    for word in fw_list:
        for item in word_df:
            if word == item[0]:
                fw_dic[word] = item[1]

    return fw_list, fw_dic

if __name__ == "__main__":
    print u"请选择一个分词文本..."
    T = TextSta(tkFileDialog.askopenfilename(title=u"选择文件"))  # 类TextSta
    w_df = T.wordsdf()  # 获取DF统计
    main(w_df)
