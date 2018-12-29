#! usr/bin/env python3
# -*-coding:utf-8-*-

"""
描述：从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是否是连续的。
2-10为数字本身，A为1，JQK对应11、12、13，大小王可看成任意数字。
思路：先排序，再遍历，大小王用0表示。
"""


def is_continuous(array):
    if not array:
        return False
    else:
        array.sort()  # 排序
        zero = 0  # 大小王个数
        small = 0
        big = small + 1
        gap = 0  # 相邻牌的空缺总数
        while big < len(array):
            if array[small] == array[big] != 0:  # 如果两张牌相等而且不是大小王
                return False
            elif array[small] == 0:
                zero += 1
            else:
                gap += array[big] - array[small] - 1
            small += 1
            big = small + 1
        # 如果相邻牌空缺总数<=大小王数量，那么连续，否则不连续
        return True if gap <= zero else False


array = [0, 1, 2, 4, 0]
print('Yes') if is_continuous(array) else print('No')
