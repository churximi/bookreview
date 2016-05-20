#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
学习：python执行CMD命令command，可以用&连接多个命令
功能：python调用CMD命令来执行本地LTP功能
时间：2016年4月13日 19:07:41
"""

import os

project_path = "d:\\myprojects\\LTP"    # 项目文件夹目录

# 可设置ltp_test、（cws、pos、par、ner）_cmdline，但是注意各自能用的参数，没有的参数请置空""
model_exe = "ltp_test"    # 又如cws_cmdline

threads_num = " --threads "+str(3)                                    # 更改线程数
last_stage = " --last-stage "+"all"                                    # 最终步骤，可设置ws、pos、ner、dp、srl、all
input_path = " --input "+"d:\\myprojects\\LTP\\file\\test.txt"        # 输入文件
seg_lexicon = ""                                                      # 分词用户词典
pos_lexicon = ""                                                      # 词性标注用户词典
output_path = "D:\\myprojects\\LTP\\result\\out.txt"                  # 输出文件

command = "cd "+project_path+" & "+model_exe+threads_num+input_path+last_stage+" > "+output_path
os.system(command)
