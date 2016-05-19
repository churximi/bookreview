#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：综合主程序，利用信息增益IG选特征词，并获取句子的各种向量表示
时间：2016年5月18日 20:25:14
"""

import tkFileDialog
from Functions.TextSta import TextSta
from Functions import GetLineList
from Functions import Wrtie
from Functions.FeatureValues import Values
from Functions import FeatureWords_IG

# 主程序
print u"请选择一个分词文本..."
T = TextSta(tkFileDialog.askopenfilename(title=u"选择文件"))    # 类TextSta
word_df = T.wordsdf()    # 获取DF统计
sentences = T.sen()      # 获取句子列表

# 选择特征词（选择DF高的若干个）
FW = FeatureWords_IG.main(word_df)
fw_list, fw_dic = FW[0], FW[1]    # 特征词列表以及字典（字典里存储有DF值）

# 读取句子的类别标注
print u"请选择句子类别文本..."
typelist = GetLineList.main()
if len(typelist) == len(sentences):
    print u"类别数量正确 = 句子数量 √ "
else:
    print u"类别数量有误，请检查。"

V = Values(fw_list, sentences, fw_dic, typelist)
binary_vec = V.binary_vec()
tf_vec = V.tf_vec()
tfidf_vec = V.tfidf_vec()

typename = raw_input(u"请输入类别名称：\n").decode("utf-8")
filename1 = typename + u"_" + str(len(sentences)) + u"句_二值_" + str(len(fw_list)) + u"特征词.arff"
Wrtie.main(filename1, binary_vec, fw_list)
filename2 = typename + u"_" + str(len(sentences)) + u"句_TF_" + str(len(fw_list)) + u"特征词.arff"
Wrtie.main(filename2, tf_vec, fw_list)
filename3 = typename + u"_" + str(len(sentences)) + u"句_TFIDF_" + str(len(fw_list)) + u"特征词.arff"
Wrtie.main(filename3, tfidf_vec, fw_list)

print u"程序结束！"

if __name__ == "__main__":
    pass
