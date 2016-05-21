#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：word2vec实验
时间：2016年5月21日 13:00:30
"""

import gensim
import logging
import codecs
import tkFileDialog
from Functions.TextSta import TextSta
from Functions import GetLineList

# 主程序
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# 调用文本分析类
print u"请选择大语料的分词文本..."
T = TextSta(tkFileDialog.askopenfilename(title=u"选择文件"))
sentences = T.sen()    # 获取句子列表
words = T.allwords()    # 所有词汇列表
print u"句子总数：", len(sentences)
print u"词汇总数：", len(words)

model = gensim.models.Word2Vec(sentences, min_count=5)

# 打开文件
print u"请选择预选特征词文件..."
fw_list = GetLineList.main()    # 获取特征词列表

f1 = codecs.open(u"相似词统计.txt", "a", "utf-8")
for word in fw_list:
    # print model[u'书']
    # print model.similarity(u"书", u"不错")
    f1.write(word + "\t")
    for item in model.most_similar(word, topn=20):
        if item[0] in fw_list:
            # f1.write(item[0] + u"\t★\t" + str(item[1]))
            f1.write(item[0] + "\t")

    f1.write("\n")

f1.close()
