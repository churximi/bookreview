# -*- coding: utf-8 -*-

"""
功能：list排序功能，sort()与sorted()
时间：2016年4月15日 16:26:31
"""

print u"测试1：sort()"
# sort()不会返回对象，所以list2 = list1.sort()是无意义的
# list.sort()会改变原来的list，所以list1将改变
list1 = [2, 1, 3, 5, 4, 1]
print u"列表1：", list1

# sorted(list)会返回一个新的列表，原来的list不变
list3 = [2, 1, 3, 5, 4, 1]
list4 = sorted(list3)
print u"列表3：", list3
print u"列表4：", list4

# 反向排序
list5 = [2, 1, 3, 5, 4, 1]
list5.sort(reverse=True)
print u"列表5：", list5

# 复杂情况反向排序
students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
list6 = sorted(students, key=lambda student: student[2], reverse=True)    # student是一个随意命名
print u"列表6：", list6

# 多次排序
L = [('d', 2), ('a', 4), ('b', 3), ('c', 2)]
list7 = sorted(L, key=lambda x: (x[1]))
list8 = sorted(L, key=lambda x: (x[1], x[0]))    # 先按照第二个元素排序，再按第一个元素排序
print u"列表7：", list7                           # 用来查看第一次排序结果
print u"列表8：", list8
