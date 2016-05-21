#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：利用词向量简单对文本进行扩展，将相关词加入句子
时间：2016年5月21日 14:16:47
"""

from Functions.TextSta import TextSta
import tkFileDialog
import codecs

print u"请选择分词文本..."
T = TextSta(tkFileDialog.askopenfilename(title=u"选择文件"))
sentences = T.sen()

fw_dic_ex = {}
f1 = codecs.open(u"C:\\Users\\lenovo\\Desktop\\test0518\\相关词250.txt", "r", encoding="utf-8")
for line in f1:
    linelist = line.strip().split("\t")
    fw_dic_ex[linelist[0]] = linelist[1:]
f1.close()

new_sentences = []
i = 0
for sentence in sentences:
    new_sentences.append([])
    for word in sentence:
        new_sentences[i].append(word)
        if word in fw_dic_ex:
            new_sentences[i] += fw_dic_ex[word]
    i += 1

for newsen in new_sentences:
    print " ".join(newsen)

if __name__ == "__main__":
    pass
