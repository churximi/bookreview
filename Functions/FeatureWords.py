#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：获取指定数量的特征词列表、字典
输入：word_df原始统计
时间：2016年5月17日 20:34:00
"""


def main(word_df):
    fw_num = raw_input(u"请输入要选择的特征词个数...\n")
    parts = word_df[:int(fw_num)]    # 选择部分特征词
    fw_list = [item[0] for item in parts]    # 存储特征词列表

    fw_dic = {}    # 存储特征词及其DF值
    for item in parts:
        fw_dic[item[0]] = item[1]

    return fw_list, fw_dic

if __name__ == "__main__":
    pass
