#! usr/bin/env python
# -*-coding:utf-8-*-

"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
"""
import random


def check_valid_input(data):
    """检查输入数据有效性"""
    if not data:
        return "Invalid Data"
    else:
        pass


def check_more_than_half(data, number):
    """检查数字是否真的超过了一半"""
    times = 0
    more_than_half = False
    for i in range(0, len(data)):
        if data[i] == number:
            times += 1
    if times * 2 >= len(data):
        more_than_half = True
    return more_than_half


def find_num_1(data):
    """
    思路1：保存两个值，一个是数组中的数字，一个是出现的次数。数字相同次数+1，数字不同次数-1，
    为0时保存下一数字并把次数设为1，要找的数字就是遍历完后最后一个设为1的数字。
    """
    check_valid_input(data)
    current_count_num = data[0]  # 初始化第一个数字
    times = 1
    for i in range(1, len(data)):
        if data[i] == current_count_num:
            times += 1
        else:
            times -= 1
        if not times:
            current_count_num = data[i]
            times = 1
    if check_more_than_half(data, current_count_num):
        print(current_count_num)
        return
    return "No More Than Half"


def swap(data, index1, index2):
    data[index1], data[index2] = data[index2], data[index1]


def partition(data, start, end):
    rand_index = random.randint(start, end)
    swap(data, rand_index, end)
    small = start - 1
    for i in range(start, end):
        if data[i] < data[end]:
            small += 1
            if small != i:
                swap(data, small, i)
    small += 1
    swap(data, small, end)
    return small


def find_num_2(data, start, end):
    """
    思路2，仿照快速排序，寻找排序后位于中位数位置的数字即为“出现的次数超过数组长度的一半”的数字
    """
    check_valid_input(data)
    middle_index = len(data) >> 1
    index = partition(data, start, end)
    if index == middle_index:
        # 找到中位数
        if check_more_than_half(data, data[index]):
            # 检查是否次数超过一半
            print(data[index])
            return
        return "No More Than Half"
    elif index < middle_index:
        # 中位数在右边
        find_num_2(data, index + 1, end)
    elif index > middle_index:
        # 中位数在左边
        find_num_2(data, start, index - 1)


if __name__ == '__main__':
    data = [1, 2, 3, 4, 4, 4, 5, 4, 4]
    find_num_1(data)
    find_num_2(data, 0, len(data) - 1)
