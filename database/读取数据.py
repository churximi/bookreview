#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：打开文件对话窗口来选择数据库，方便使用
更新：调用写好的函数，来连接数据库
时间：2016年5月5日 14:12:03
"""

import codecs
from Functions.ConnectDB import main

# 连接数据库
connection = main()
cur, conn = connection[0], connection[1]

# SQL查询,写入新文件
outputfile = codecs.open("output.txt", "a", encoding="utf-8")
outputfile.truncate()

SQL1 = "SELECT * from minclause"    # SQL，根据需要修改
for row in cur.execute(SQL1):
    print row.sentence
    # outputfile.write(row.sentence + "\n")

outputfile.close()
cur.close()
conn.commit()
conn.close()

print u"程序结束！"
