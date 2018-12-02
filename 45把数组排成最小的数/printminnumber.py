#! usr/bin/env python3
# -*-coding:utf-8-*-

"""
题目：输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的数字中最小的一个。
示例：输入[3, 32, 321]，输出321323。
思路：
1.写出全排列再进行比较;
2.定义新的比较规则,如果mn<nm,则m<n;否则n<m;
"""
import random


def print_min_number(array):
    if not array:
        return 'Invalid Input'
    quick_sort(array, 0, len(array) - 1)
    result = ''
    for item in array:
        result += str(item)
    return result


def partition(array, start, end):
    randindex = random.randint(start, end)
    swap(array, randindex, end)
    small = start - 1
    for i in range(start, end):
        if compare(array, i, end):
            small += 1
            if small != i:
                swap(array, small, i)
    small += 1
    swap(array, small, end)
    return small


def quick_sort(array, start, end):
    pivot = partition(array, start, end)
    if pivot > start:
        quick_sort(array, start, pivot - 1)
    if pivot < end:
        quick_sort(array, pivot + 1, end)


def swap(array, index1, index2):
    """
    交换元素
    :param array:
    :param index1:
    :param index2:
    :return:
    """
    array[index1], array[index2] = array[index2], array[index1]


def compare(array, index1, index2) -> bool:
    """
    定义新的比较规则,如果mn<nm,则m<n;否则n<m;
    :param array:
    :param index1:
    :param index2:
    :return: bool
    """
    str1 = str(array[index1]) + str(array[index2])
    str2 = str(array[index2]) + str(array[index1])
    return True if str1 < str2 else False


print(print_min_number([1, 2, 3, 4, 22]))  # 122234
print(print_min_number([3, 32, 321]))  # 321323