#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：利用stanford parser语法结构树进行分句，写入数据库
时间：2016年4月25日 21:47:42
"""

import re
import os
import pyodbc
import codecs


def newfenju(par1):
    pattern = re.compile(u'PU ，\)\(IP')
    pattern2 = re.compile(u' [^\(]*?\)')
    filepath = r"C:\Users\lenovo\Desktop\test0504\trees" + "\\" + par1
    newline = ""
    f = codecs.open(filepath, "r", "utf-8")
    for line in f:
        if u"     (IP" not in line:
            if u"    (IP" in line:
                line = line.replace(u"(IP", u"(IP 。)")
        line = line.strip()
        newline += line
    newline2 = newline

    fenju = re.findall(pattern, newline2)    # 找到所有的IP分句
    for item in fenju:
        item2 = item.replace(u"，", u"。")
        newline2 = newline2.replace(item, item2)

    aalist = []
    chongzu = re.findall(pattern2, newline2)
    for aa in chongzu:
        aa = aa.replace(")", "")
        aalist.append(aa)
    newsen = "".join(aalist)
    newsen = newsen.replace("... ...", u"……")

    clauselist = []
    sen_pat = re.compile(u"(.*?)([。？！；]|[…]{2})")
    xx = re.findall(sen_pat, newsen)
    for x in xx:
        y = "".join(x)
        y = y.lstrip(" ")    # 删除开头的空格
        if len(y) > 1:
            clauselist.append(y)

    f.close()
    return clauselist

filenames = os.listdir(r"C:\Users\lenovo\Desktop\test0504\trees")    # 语法依赖树文本

DBfile = r"C:\Users\lenovo\Desktop\test0504\sentences.accdb"
conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + DBfile + ";Uid=;Pwd=;")
print u"已建立数据库连接。"
cur = conn.cursor()

# 创建表，保存根据语法树分句后的句子
cur.execute("Create TABLE midnew(score Real,bookID SmallInt,reviewId SmallInt,senID SmallInt,"
            "clauseID SmallInt,sentence Memo)")

bianhao = []    # 提取文档编号
f1 = codecs.open(u"C:\\Users\\lenovo\\Desktop\\test0504\\3509原始句子编号.txt", "r", "utf-8")
for line1 in f1:
    temp = line1.strip().split("\t")
    bianhao.append(temp)
f1.close()

for i in range(len(filenames)):   # 根据依赖树进行新的分句，然后将从句写入数据库
    ff = str(i)+".txt"
    if ff in filenames:
        clauses = newfenju(ff)
        clauseID = 1
        for clause in clauses:
            print clause
            cur.execute("insert into midnew values('%s','%s','%s','%s','%s','%s')"
                        % (bianhao[i][0], bianhao[i][1], bianhao[i][2], bianhao[i][3], clauseID, clause))
            clauseID += 1


print u"处理完毕，处理文件个数：", len(filenames)

cur.close()
conn.commit()
conn.close()
