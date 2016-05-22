#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：Stanford CoreNLP本地调用，通过借助command line来运行
针对：中文文本，上限20万items
时间：2016年4月22日 20:27:06
"""

import os

CoreNLP_path = r"cd D:\CoreNLP"
loadjar = ' -cp "*" '
Xmx = " -Xmx4g "    # 设置最大内存
pipline = " edu.stanford.nlp.pipeline.StanfordCoreNLP "
annotators = " -annotators tokenize,ssplit,pos,ner,parse,dcoref "
inputfile = r" -file D:\CoreNLP\file\input_zh.txt "     # 输入文件
outputDir = r" -outputDirectory D:\CoreNLP\file "    # 输出路径
outformat = " -outputFormat xml "    # 有text、xml、json、conll、conllu、serialized等输出格式
props = " -props StanfordCoreNLP-chinese.properties "    # 选择properties

command = (CoreNLP_path + " & " + "java" + loadjar + Xmx + pipline +
           annotators + inputfile + outputDir + outformat + props)
os.system(command)

