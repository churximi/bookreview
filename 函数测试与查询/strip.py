# -*- coding: utf-8 -*-

"""
功能：strip()函数使用
时间：2016年4月18日 13:23:44
介绍：
（1）strip()用来删除【开头】、【结尾】处的空白字符（\n、\r、\t、'')
（2）strip(rm)用来删除【开头】、【结尾】处字符序列rm
（3）lstrip(rm)用来删除【开头】处的字符rm
（4）rstrip(rm)用来删除【结尾】处的字符rm
（5）lstrip()和rstrip()分别用来删除开头、结尾处的空白字符
注意：
（1）在删除非空白字符序列时，注意字符串两边是否有空白字符干扰
（2）strip(rm)中，rm是一个序列，只要字符串两边的字符在序列内，就会删除，而不管其顺序如何（★）
"""

string = "   测试文本   \n \r \t"
s1 = string.strip()
print "删除空白字符后:", s1
print "剩余的字符长度:", len(s1.decode("utf-8"))

# 注意，删除的是开头和结尾的字符，对中间的字符串不起作用
string2 = "这是这01这是02这是"
s2 = string2.strip("是这")    # 效果等同于strip("这是")
print "删除两个【这是】:", s2

s3 = string2.lstrip("这是")
print "删除开头【这是】:", s3

s4 = string2.rstrip("这是")
print "删除结尾【这是】:", s4
