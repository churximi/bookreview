# -*- coding:utf-8 -*-

"""
功能：for...else语句
"""

for i in range(5):
    print i
else:
    print u"循环完整执行一次。"

for j in range(6):
    for k in range(6):
        print j, k
        if j == 3:
            print u"内重循环即将被break"
            break
    else:
        print u"内重循环完整执行一次。"
else:
    print u"外重循环完整执行一次。"
