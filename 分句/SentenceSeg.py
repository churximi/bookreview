# -*- coding: utf-8 -*-

"""
功能：读入语法结构树，根据IP重新分句。
时间：2016年4月12日 19:34:00
"""

import re
import codecs

firstnodes = {}  # 定义空字典，存储每行首节点信息：节点名，节点所在行数，节点前的空格
firstnodeslist = []
allnodes = []  # 存放所有节点
rowlist = []
tags = ["ROOT", "IP", "NP", "PN", "VP", "VC", "QP", "CD", "CLP", "M", "DNP", "PP", "P", "NN", "DEG",
        "PU", "NR", "VV", "LCP", "CP", "ADVP", "ADJP", "DP", "NNS", "NNP", "NNPS", "NT", "CC", "VE",
        "VA", "AS", "VRD", "RP", "DT", "EX", "FW", "IN", "JJ","JJR", "JJS", "LS", "MD", "PDT", "POS",
        "PRP", "PRP$", "RB", "RBR", "RBS", "SYM", "TO", "WDT", "WP", "WP$", "WRB", "UH", "VB",
        "VBD", "VBG", "VBN", "VBP", "VBZ"]

f = open("file\\test.txt", "r")
for line in f:  # 对于每一行
    newline = []
    line = line.replace("(", "").replace(")", "").replace("\n", "")  # 删除括号和换行符
    line = re.split(" ", line)  # 切分元素

    for lineitem in line:
        if lineitem == "":
            newline.append(lineitem)
        else:
            if lineitem not in allnodes:  # 如果节点暂时没有重名
                allnodes.append(lineitem)
                newline.append(lineitem)
            else:
                newline.append(lineitem)

    rowlist.append(newline)

realnodes = []  # 所有非空节点
for a in rowlist:
    for aa in a:
        if not aa == "":
            realnodes.append(aa)

IPnum = 0  # 统计IP数量
for b in realnodes:
    if "IP" in b:
        IPnum += 1
print IPnum

if IPnum > 1:    # 当IP节点大于1时，才重新分句
    for j in range(len(realnodes)):    # 将IP节点前的标点改为句号。
        if "IP" in realnodes[j]:
            if "，" in realnodes[j-1]:
                realnodes[j-1] = "。"

sen_nodes = []
for c in realnodes:
    if c not in tags:
        sen_nodes.append(c)
newsen = "".join(sen_nodes)
print newsen

newtxt = codecs.open("file\\newtxt.txt", "a", "utf-8")
newtxt.truncate()
newtxt.write(newsen.decode("utf-8"))
newtxt.close()
