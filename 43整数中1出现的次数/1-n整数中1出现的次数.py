# usr/bin/env python
#-*-coding:utf-8-*-

"""
题目：输入一个整数n，求1~n这n个整数的十进制表示中1出现的次数。
示例：输入12,1~12这些整数中包含1的数字有1-10-11-12，共出现5次。
"""


def number1_times(n):
	"""
	每个数从个位开始统计,每次缩减1位。
	如果每个数有O(logn)位,则复杂度为O(nlogn)
	"""
    times = 0
    for i in range(1, n + 1):
        while(i > 0):
            if i % 10 == 1:
                times += 1
            i = i // 10
    return times

print(number1_times(12))
