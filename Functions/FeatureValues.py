#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：计算各种特征值，如二值、TF、TF-IDF
输入：特征词列表、句子列表、特征词字典、类别列表
时间：2016年5月17日 20:58:58
"""

import math


class Values:
    # 定义基本属性
    __fw_list = []
    __fw_dic = {}
    __sen_list = []
    __type_list = []

    # 定义构造方法
    def __init__(self, fwlist, senlist, fwdic, typelist):
        self.fw_list = fwlist
        self.sen_list = senlist
        self.fw_dic = fwdic
        self.type_list = typelist

    def binary_vec(self):    # 计算二值，将句子表示为（0,1)的向量
        sentence_vector = []  # 存储句子向量
        for i in range(len(self.sen_list)):
            sentence_vector.append([])
            for word in self.fw_list:
                if word in self.sen_list[i]:
                    sentence_vector[i].append(1)  # 特征词出现则记为1
                else:
                    sentence_vector[i].append(0)
            sentence_vector[i].append(self.type_list[i])  # 列表末尾加入类别
        print u"句子二值向量表示完毕。"
        return sentence_vector

    def tf_vec(self):    # 计算TF绝对词频，将句子表示为TF的向量
        sentence_vector = []
        for i in range(len(self.sen_list)):
            sentence_vector.append([])
            for word in self.fw_list:
                sentence_vector[i].append(self.sen_list[i].count(word))  # 计算每个句子中特征词的TF
            sentence_vector[i].append(self.type_list[i])  # 列表末尾加入类别
        print u"句子TF向量表示完毕。"
        return sentence_vector

    def tfidf_vec(self):
        # 将句子表示为TF-IDF的向量（其中TF没有归一化）
        sen_num = float(len(self.sen_list))  # 句子个数
        sentence_vector = []  # 存储句子向量
        for i in range(len(self.sen_list)):
            sentence_vector.append([])
            for word in self.fw_list:
                tf = self.sen_list[i].count(word)
                idf = math.log(sen_num / int(self.fw_dic[word]), 10)  # 以10为底的对数
                tf_idf = tf * idf
                sentence_vector[i].append(tf_idf)  # 计算每个句子中特征词的TF
            sentence_vector[i].append(self.type_list[i])  # 列表末尾加入类别
        print u"句子TF-IDF向量表示完毕。"
        return sentence_vector

if __name__ == "__main__":
    pass
