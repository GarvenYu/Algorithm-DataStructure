#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：0,1,...,n-1这n个数字排成一个圆圈，从数字0开始，每次从圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。
示例：0 1 2 3 4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前四个数字依次是2 0 4 1，剩下的是3.
思路:用一个list模拟环形链表，当到达尾部时返回头部循环遍历。
"""


def last_number(array, m):
    if not array or m < 1:
        return None
    else:
        current = 0  # 当前去掉的元素位置，也是新的计数元素位置
        while len(array) > 1:
            if current + m <= len(array):
                # 如果不用从头循环
                current += m - 1
                array.pop(current)
            else:
                # 如果需要从头循环，找到删除位置
                current = (current + m) % len(array) - 1
                array.pop(current)
        return array


array = [0, 1, 2, 3, 4]
m = 3
print(last_number(array, m))  # 3
