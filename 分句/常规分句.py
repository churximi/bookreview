#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：对一个纯文本里面的句子，按照常规的。？！；……五种符号进行分句
时间：2016年5月4日 15:07:25
"""

import codecs
import tkFileDialog
import re
import pyodbc

print u"请选择文本文件..."                       # 路径最好不含中文
file_path = tkFileDialog.askopenfilename()      # 打开文件选择界面
f = codecs.open(file_path, "r", "utf-8")

text = ""
for line in f:
    text += line.strip()
f.close()


senlist = []
sen_pat = re.compile(u"(.*?)([。？！；]|[…]{2})")    # 五种标点符号
sentences = re.findall(sen_pat, text)
for sentence in sentences:
    senlist.append("".join(sentence))    # 存储句子列表

DBfile = u"C:\\Users\\lenovo\\Desktop\\test0504\\sentences.accdb"    # 数据库
conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + DBfile + ";Uid=;Pwd=;")
print u"已建立数据库连接。"
cur = conn.cursor()
cur.execute("Create TABLE maxnew(score Real,bookID SmallInt,reviewid SmallInt,senID SmallInt,sentence Memo)")

bianhao = []
i = 0
f1 = codecs.open(u"C:\\Users\\lenovo\\Desktop\\test0504\\3509原始句子编号.txt", "r", "utf-8")
for line in f1:
    temp = line.strip().split("\t")
    cur.execute("insert into maxnew values('%s','%s','%s','%s','%s')"
                % (temp[0], temp[1], temp[2], temp[3], senlist[i]))
    i += 1
f1.close()

cur.close()
conn.commit()
conn.close()
