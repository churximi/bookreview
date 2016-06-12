#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：enumerate函数的用法
时间：2016年6月12日 18:03:11
"""

list1 = ["这", "是", "一个", "测试"]
for index, item in enumerate(list1):
    print index, item

for index2, item2 in enumerate(list1, 1):  # 第二个参数指定起始编号
    print index2, item2

# 相当于
for i in range (len(list1)):
    print i ,list1[i]

# 统计文件行数
f = open(u"C:\\Users\\lenovo\\Desktop\\9784分词.txt", "r")
# count = len(f.readlines())
# print count
count1 = 0
for x, line in enumerate(f):
    count1 += 1
print count1
