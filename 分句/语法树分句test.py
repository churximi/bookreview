# -*- coding: utf-8 -*-

"""
功能：利用stanford parser语法结构树进行分句，将新的分句存入文本
时间：2016年4月15日 12:55:12
"""

import codecs
import re
import os


def newfenju(par1):
    pattern = re.compile(u'PU ，\)\(IP')
    pattern2 = re.compile(u' [^\(]*?\)')
    filepath = r"C:\Users\lenovo\Desktop\test0423\alltrees" + "\\" + par1
    newline = ""
    f = open(filepath, "r")
    for line in f:
        if "     (IP" not in line:
            if "    (IP" in line:
                line = line.replace("(IP", "(IP 。)")
        line = line.strip()
        newline += line
    newline2 = newline.decode("utf-8")

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

    sen_pat = re.compile(u'.*?[。！？；…]')    # 新的分句写入文本
    xx = re.findall(sen_pat, newsen)
    for x in xx:
        x = x.lstrip(" ")    # 删除开头的空格
        if len(x) > 1:
            if u"…" in x:
                newfile.write(x+u"…"+"\n")
            else:
                newfile.write(x+"\n")

    f.close()
    return

newfile = codecs.open(u"C:\\Users\\lenovo\\Desktop\\newsenseg.txt", "a", "utf-8")
filenames = os.listdir(r"C:\Users\lenovo\Desktop\test0423\alltrees")
for i in range(len(filenames)):
    ff = str(i)+".txt"
    if ff in filenames:
        print u"正在处理文件：", ff
        newfenju(ff)

print u"****处理文件个数：", len(filenames)
newfile.close()
