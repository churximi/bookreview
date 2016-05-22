#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：连接数据库函数
返回：cur，conn
时间：2016年5月5日 14:12:24
"""

import pyodbc
import tkFileDialog


def main():
    print u"请选择数据库文件..."    # 通过文件对话窗口选择数据库文件，返回数据库路径
    dbfile_path = tkFileDialog.askopenfilename(title=u"选择文件")    # 路径最好不含中文
    if dbfile_path:
        conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + dbfile_path + ";Uid=;Pwd=;")
        print u"已建立数据库连接。"
        cur = conn.cursor()
        return cur, conn
    else:
        print u"★注意：本次操作没有选择文件！"

if __name__ == "__main__":
    pass

"""
更新日志：
2016年5月5日 14:13:01，增加文件选择窗口，tkFileDialog.askopenfilename()
2016年5月5日 14:33:56，添加提示（未选择文件直接退出时）
"""
