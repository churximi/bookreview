#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：Stanford CoreNLP本地调用，通过借助command line来运行
针对：英文文本
时间：2016年4月22日 19:42:48
"""

import os

CoreNLP_path = r"cd D:\CoreNLP"
loadjar = ' -cp "*" '
Xmx = " -Xmx2g "
pipline = " edu.stanford.nlp.pipeline.StanfordCoreNLP "
annotators = " -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref "
inputfile = r" -file D:\CoreNLP\file\input.txt "
outputDir = r" -outputDirectory D:\CoreNLP\file "    # 输出路径
outformat = " -outputFormat json "    # 有text、xml、json、conll、conllu、serialized等输出格式

command = CoreNLP_path + " & " + "java" + loadjar + Xmx + pipline + annotators + inputfile + outputDir + outformat
os.system(command)
