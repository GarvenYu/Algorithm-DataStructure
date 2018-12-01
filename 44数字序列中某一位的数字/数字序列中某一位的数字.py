# usr/bin/env python
#-*-coding:utf-8-*-

"""
题目：数字以0123456789101112131415...的格式序列化到一个字符序列中。请写一个函数，求任意第n位对应的数字。
示例：第5位(从0开始计数)是5，第13位是1，第19位是4，等等。
"""


def number_of_index_n(n):
    power = 1  # 幂指数,代表数字是几位数
    while True:
        if power == 1:
            length = 10
        else:
            # 个位数有10位,十位数有180位，百位数有2700位...
            length = power * (10 ** power - 10 ** (power - 1))
        if n > length:
            n -= length
            power += 1
        else:
            break
    # 求出开头数字
    start = 10 ** (power - 1)
    a = n // power
    b = n % power
