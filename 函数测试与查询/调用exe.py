# -*- coding: utf-8 -*-

"""
功能：Python调用win7系统exe程序
时间：2015年12月23日 17:57:56
备注1：如果路径中含有中文，也可以将第一行声明编码改为gbk或gb2312，正式代码中
就不用单独encoding了。
"""

import os

os.popen(u"D:\腾讯QQ\Bin\QQScLauncher.exe".encode("gbk"))    # 路径中含有中文
# os.popen("D:\KGMusic\KuGou.exe")    # 路径中不含中文

# os.popen(u"D:\\腾讯QQ\\Bin\\QQScLauncher.exe".encode("gbk"))    # 路径中含有中文
# os.popen("D:\KGMusic\KuGou.exe")    # 路径中不含中文
# os.popen(r"D:\myprojects\LTP\run.bat")    # 调用bat
# os.system(r"D:\myprojects\LTP\run.bat ")
