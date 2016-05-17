#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：自定义写入文本，格式为arff
输入：文件名，句子向量，特征词列表
时间：2016年5月17日 21:12:56
"""

import codecs


def main(filename, sentence_vector, fwlist):    # 定义写入文本的方法
    writefile = codecs.open(filename, "a", "utf-8")
    writefile.truncate()

    writefile.write(u"@relation " + filename + "\n\n")
    for everyword in fwlist:
        writefile.write(u"@attribute " + everyword + u" numeric\n")
    writefile.write(u"@attribute *type* {True,False}\n\n@data\n")  # 类别属性，加*是避免与特征词冲突
    for vector in sentence_vector:
        for value in vector[:-1]:
            writefile.write(str(value) + ",")
        writefile.write(str(vector[-1]) + "\n")
    writefile.close()

    return

if __name__ == "__main__":
    pass
