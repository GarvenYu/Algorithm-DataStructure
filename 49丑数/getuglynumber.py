#! usr/bin/env python3
# -*-coding:utf-8-*-

"""
题目：我们把只包含因子2、3、5的数称为丑数。求按从小到大的顺序的第1500个丑数。
示例：4、6、8都是丑数，但14不是，因为它包含因子7.习惯上我们把1当做成第一个丑数。
方法1：时间消耗高但是直观
"""


def is_ugly_number(number):
    while number % 2 == 0:
        number //= 2
    while number % 3 == 0:
        number //= 3
    while number % 5 == 0:
        number //= 5
    return True if number == 1 else False


def get_ugly_number(index):
    number = 1
    while index > 0:
        if is_ugly_number(number):
            index -= 1
        number += 1
    return number - 1


print(get_ugly_number(15))