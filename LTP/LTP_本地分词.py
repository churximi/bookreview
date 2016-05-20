#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：LTP本地分词cws_cmdline，输入文本需要每行一句。（不能自动分句）
时间：2016年4月13日 20:22:39
"""

import os

project_path = "d:\\myprojects\\LTP"    # 项目文件夹目录

model_exe = "cws_cmdline"               # 分词模块，相当于ltp_test的last_stage=ws，但是输出格式不同

threads_num = " --threads "+str(3)                                    # 更改线程数
input_path = " --input "+"d:\\myprojects\\LTP\\file\\test.txt"        # 输入文件
seg_lexicon = " --segmentor-lexicon "+"D:\\myprojects\\LTP\\file\\seg_lexicon.txt"     # 分词用户词典
output_path = "D:\\myprojects\\LTP\\result\\out.txt"                  # 输出文件

command = "cd "+project_path+" & "+model_exe+threads_num+input_path+seg_lexicon+" > "+output_path
os.system(command)
