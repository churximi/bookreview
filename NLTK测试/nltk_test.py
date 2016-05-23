# -*- coding: utf-8 -*-

"""
功能：练习NLTK基本使用
时间：2016年4月17日 13:41:26
"""

import NLTK测试

f = open(r"file\test.txt")
text = ""
for line in f:
    text += line.strip()+" "
print text
text = text.split(" ")

fdist1 = NLTK测试.FreqDist(text)
print fdist1
print fdist1["的"]

"""
print len(set(text))

text1 = "English word"
print len(text1)

word_fre = nltk.probability.FreqDist(text)
print type(word_fre)
print " ".join(word_fre)
vocabulary = word_fre.keys()
xx = vocabulary[:8]
print " ".join(xx)

"""
