#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
功能：字典用法
时间：2016年5月17日 22:31:57
"""

firstnodes = {"node1": [0, 1], "node2": [2, 3]}
item = "ROOT"
firstnodes[item] = [4, 5]
print firstnodes[item][1]
if item in firstnodes:
    firstnodes[item].append(6)
print firstnodes[item]
