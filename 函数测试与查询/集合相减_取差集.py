#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：测试集合取差集（两个list/set“相减”）
时间：2016年5月13日 23:05:55
"""

a = [1, 2]
b = [1, 2, 3, 4]

print list(set(b).difference(set(a)))
print list(set(b) - set(a))

"""
备注：
set可以相减，但是list不可以
得到的是b里面有但是a里面没有的元素集合
"""
