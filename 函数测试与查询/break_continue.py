# -*- coding:utf-8 -*-

"""
功能：break语句与continue语句
区分：break跳过最深层循环，该层循环的剩余次数不再执行；continue跳过当前循环的这一次
，但剩余次数继续执行。
注意：在多重循环中，某一层的break并不能终止其上一层的循环。
更新：2016年4月2日 12:51:41
"""

for letter in 'Python':    # 例1
    if letter == 'h':
        break
    print u'当前字母：', letter
print u'*****例1结束。*****'

var = 10  # 例2
while var > 0:
    print u'当前值', var
    var -= 1
    if var == 5:
        continue
print u'*****例2结束。*****'

# 例3循环
for i in range(4):
    for j in range(4):
        for k in range(4):
            if i == j == k == 2:
                break
            else:
                print i, j, k
