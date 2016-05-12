#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：通过五种标点分句
时间：2016年5月12日 12:47:13
"""

import codecs
import tkFileDialog
import re

print u"请选择文本文件..."                       # 路径最好不含中文
file_path = tkFileDialog.askopenfilename()      # 打开文件选择界面
f = codecs.open(file_path, "r", "utf-8")

fnew = codecs.open("fenju.txt", "a", "utf-8")
for line in f:
    line = line.strip() + u"。"
    sen_pat = re.compile(u"(.*?)([。？！；]|[…]{2})")    # 五种标点符号
    sentences = re.findall(sen_pat, line)
    for sentence in sentences:
        x = "".join(sentence)
        x = x.strip()
        if len(x) > 1:
            fnew.write(x + "\n")

f.close()
fnew.close()
