#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：结巴分词测试
时间：2016年5月21日 15:44:24
问题：不能在Anaconda python里正常输出词性标注
"""

import jieba
import jieba.posseg as pseg

# 分词模式
seg = jieba.cut("这是一本关于信息检索的书", cut_all=True)  # cut_all=True，全模式
print(u"全模式分词: " + "/ ".join(seg))

seg = jieba.cut("这是一本关于信息检索的书", cut_all=False)  # cut_all=False，精确模式
print(u"精确模式分词: " + "/ ".join(seg))

seg = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print(", ".join(seg))

seg = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print(", ".join(seg))

# 添加自定义词典
jieba.load_userdict("userdic.txt")
seg = jieba.cut("这是一本关于信息检索的书")
print "/ ".join(seg)

# 词性标注
words = pseg.cut("这是一本关于信息检索的书")
for word, flag in words:
    print ('%s %s' % (word, flag))
