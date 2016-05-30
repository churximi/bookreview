#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：基本运算符
时间：2016年5月30日 19:39:24
"""

import math

# 除法
print u"1/2=", 1/2
print u"1.0/2=", 1.0/2
print u"float(1)/2=", float(1)/2

# 整除
print u"1//2=", 1//2
print u"1.0//2=", 1.0//2

# 取余（模除）运算符
print u"10 % 3=", 10 % 3

# 幂（乘方）运算符
print u"2**3=", 2**3

# power函数
print u"2的3次方=", pow(2, 3)

# 绝对值
print u"-2的绝对值=", abs(-2)

# 四舍五入
print u"1.9四舍五入向下取值：", math.floor(1.9)    # 向下取值
print u"1.9四舍五入向上取值：", math.ceil(1.9)    # 向上取值

# 四舍五入（round）
print u"round(1.9)=", round(1.9)

# 开方
s = math.sqrt
print u"sqrt(9)=", s(9)

if __name__ == "__main__":
    pass
