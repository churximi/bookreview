#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：中文词频统计，统计单词的DF值，即单词在多少个句子中出现
输入：已经分词的文本，每行一句
时间：2016年5月16日 20:34:51
"""

import codecs
from Functions import Text2SenList
from Functions import GetAllWords

print u"请选择已经分词的句子文本..."
sentences = Text2SenList.main()    # 获取句子列表，每个句子也是一个列表

# 去除停用词和无意义词
print u"再次打开该文本..."
word_tf_list = GetAllWords.main()
words = [item[0] for item in word_tf_list]    # 取出列表里所有的第一项（即词汇）

word_fre = []    # 词频列表
for word in words:
    count = 0
    for sentence in sentences:
        if word in sentence:
            count += 1
    word_fre.append([word, str(count)])    # 存储形式[word，DF]
word_fre.sort(key=lambda x: int(x[1]), reverse=True)    # 词频从大到小排序

# 写入文本
filename = u"DF统计_" + str(len(words)) + u"词_" + str(len(sentences)) + u"句.txt"    # 自动命名
f1 = codecs.open(filename, "a", "utf-8")
f1.truncate()
for y in word_fre:
    text = "\t".join(y)
    f1.write(text+"\n")

print u"程序结束！"
