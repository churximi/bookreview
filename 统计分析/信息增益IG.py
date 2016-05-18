#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：计算特征词的信息增益，以此来选择特征词
时间：2016年5月18日 17:32:11
"""

import math
import tkFileDialog
from Functions import GetLineList
from Functions.TextSta import TextSta

# 主程序
# 获取所有句子列表
print u"请选择一个分词文本..."
T = TextSta(tkFileDialog.askopenfilename(title=u"选择文件"))    # 类TextSta
sentences = T.sen()
word_df = T.wordsdf()    # 获取DF统计

# 读取句子的类别标注
print u"请选择句子类别文本..."
typelist = GetLineList.main()
if len(typelist) == len(sentences):
    print u"类别数量正确 = 句子数量 √ "
else:
    print u"类别数量有误，请检查。"

sentences_true = []    # 挑出True类别的句子
for i in range(len(typelist)):
    if typelist[i] == "True":
        sentences_true.append(sentences[i])
print u"True类别句子数量：", len(sentences_true)

# 总的特征词及其DF
fw_list = [item[0] for item in word_df]
fw_dic = {}  # 存储特征词及其DF值
for item1 in word_df:
    fw_dic[item1[0]] = item1[1]

# 统计True类别句子里，特征词的DF
word_df_true = {}
for word in fw_list:
    count = 0
    for sentence in sentences_true:
        if word in sentence:
            count += 1
    word_df_true[word] = count    # 存储为字典

# 计算不考虑特征时的熵
N_total = len(sentences)    # 句子总数
N_true = len(sentences_true)    # True类别句子总数
N_false = N_total - N_true    # False类别句子总数
print u"False类别句子数量：", N_false

p1 = N_true / float(N_total)
p2 = N_false / float(N_total)
S_entropy = (-p1*math.log(p1, 2)) + (-p2*math.log(p2, 2))
print u"不考虑特征时的熵：", S_entropy

# 计算考虑特征词后的熵
ex_entropy = 0
for word in fw_list:    # 对于某个特征词
    IG = 0
    p_total = int(fw_dic[word]) / float(N_total)  # 特征词的文档概率
    if word_df_true[word] == 0 or word_df_true[word] == int(fw_dic[word]):
        ex_entropy1 = 0
    else:
        p_t_1 = word_df_true[word] / float(fw_dic[word])    # 含有特征词且属于True类的概率
        p_f_1 = 1 - p_t_1                                   # 含有特征词且属于False类的概率
        ex_entropy1 = -p_total*(p_t_1*math.log(p_t_1, 2) + p_f_1*math.log(p_f_1, 2))
    if word_df_true[word] == N_true or (int(fw_dic[word]) - word_df_true[word] == N_false):
        ex_entropy2 = 0
    else:
        p_t_0 = (N_true - word_df_true[word]) / float(N_total - int(fw_dic[word]))
        p_f_0 = 1 - p_t_0
        ex_entropy2 = -(1 - p_total)*(p_t_0*math.log(p_t_0, 2) + p_f_0*math.log(p_f_0, 2))

        IG = S_entropy - ex_entropy1 - ex_entropy2
        print word, "\t", IG, "\t", fw_dic[word]

if __name__ == "__main__":
    pass
