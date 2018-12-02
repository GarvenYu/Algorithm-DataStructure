#! usr/bin/env python3
# -*-coding:utf-8-*-

"""
题目：数字以0123456789101112131415...的格式序列化到一个字符序列中。请写一个函数，求任意第n位对应的数字。
示例：第5位(从0开始计数)是5，第13位是1，第19位是4，等等。
"""


def number_of_index_n(n):
    power = 1  # 幂指数,代表数字是几位数
    while True:
        if power == 1:
            length = 10  # 个位数10位
        else:
            # 十位数有180位，百位数有2700位...
            length = power * (10 ** power - 10 ** (power - 1))
        if n > length:
            n -= length
            power += 1
        else:
            break
    if power == 1:
        start = 0  # 个位数开头数字 e.g. 0
    else:
        start = 10 ** (power - 1)  # 求出开头数字,e.g. start = 10,100,1000...
    front_number = n // power  # 从start开始前面有a个power位数字,e.g. 10 11 12 13
    left_number = n % power  # 余数位, 1
    result = start + front_number  # 14
    return int(str(result)[left_number])


print(number_of_index_n(19))  # 4
print(number_of_index_n(0))  # 0
print(number_of_index_n(1001))  # 7
