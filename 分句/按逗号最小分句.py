#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：按逗号对句子进行最小分句，并写入数据库
时间：2016年4月25日 13:44:43
"""

import pyodbc
import re

DBfile = r"C:\Users\lenovo\Desktop\test0423\sentences.accdb".decode("utf-8")
conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + DBfile + ";Uid=;Pwd=;")
print u"已建立数据库连接。"
cur = conn.cursor()

# 创建表，保存最小句子

cur.execute("Create TABLE minclause(score Real,bookID SmallInt,reviewId SmallInt,senID SmallInt,"
            "clauseID SmallInt,sentence Memo)")


sen_pat = re.compile(u'.*?[，。！？；…]')    # 分句正则表达式
SQL1 = "SELECT * from maxsentence"

i = 0
readout = []    # 存入列表
for row in cur.execute(SQL1):
    readout.append([])
    for item in row:
        readout[i].append(item)
    i += 1

for j in range(len(readout)):
    clauseID = 1
    allclauses = re.findall(sen_pat, readout[j][4])
    for clause in allclauses:
        if len(clause) > 1:    # 排除半个省略号…
            if u"…" in clause:
                clause += u"…"
            cur.execute("insert into minclause values('%s','%s','%s','%s','%s','%s')"
                        % (readout[j][0], readout[j][1], readout[j][2], readout[j][3], clauseID, clause))
        clauseID += 1

print u"处理完毕。"
cur.close()
conn.commit()
conn.close()
