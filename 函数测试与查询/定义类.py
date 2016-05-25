# -*- coding:utf-8 -*-

"""
功能：类的定义
版本：2016年4月2日 15:53:30
"""


class People:
    # 定义基本属性
    name = ''
    age = 0

    # 定义私有属性
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s is speaking: I am %d years old, and my weight is %d" % (self.name, self.age, self.__weight))

p = People('tom', 10, 20)
p.speak()
