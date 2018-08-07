#! usr/bin/env python
# -*-coding:utf-8-*-

"""
输入一个整数数组，实现一个函数来调整数组中数字的顺序，使得所有奇数位于数组的前半部分，偶数位于后半部分。
定义首尾两个指针，对向查询并交换。
"""


def reorder_array(data_list):
    """满足题目的解法"""
    if not data_list:
        return data_list
    head = 0
    tail = len(data_list) - 1
    while head < tail:
        while head < tail and data_list[head] & 0x01 == 1:
            # 当前指向奇数
            head += 1
        while head < tail and data_list[tail] & 0x01 != 1:
            # 当前指向偶数
            tail -= 1
        if head < tail:
            data_list[head], data_list[tail] = data_list[tail], data_list[head]
    return data_list


def reorder_array_expansibility(data_list, function):
    """扩展性好的解法"""
    if not data_list:
        return data_list
    head = 0
    tail = len(data_list) - 1
    while head < tail:
        while head < tail and function(data_list, head):
            # 当前指向奇数
            head += 1
        while head < tail and not function(data_list, tail):
            # 当前指向偶数
            tail -= 1
        if head < tail:
            data_list[head], data_list[tail] = data_list[tail], data_list[head]
    return data_list


def general_function(data_list, head):
    """可根据具体逻辑进行修改"""
    return data_list[head] & 0x01 == 1

if __name__ == '__main__':
    data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(reorder_array_expansibility(data_list, general_function))
