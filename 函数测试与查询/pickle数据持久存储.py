#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：将一些重要的数据存储到本地，以便再次使用
模块：pickle
时间：2016年5月24日 19:06:43
"""

import pickle

data1 = [u"这", u"是", u"测试"]
with open('data1.pkl', 'wb') as output:
    pickle.dump(data1, output)    # 存入output文件

print u"程序结束！"

f = file("data1.pkl", "rb")
data2 = pickle.load(f)
print u"data2的数据类型：", type(data2), u"\n====分隔符===="
print u"data2的数据内容：", "".join(data2)
