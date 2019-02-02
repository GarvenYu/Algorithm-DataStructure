# usr/bin/env python
# -*-coding:utf-8-*-

"""
题目：输入一个整数数组，数组里有正数和负数。数组中的一个或连续多个数字组成一个子数组。求所有子数组中和的最大值。
要求：时间复杂度为O(n)
示例：输入[1,-2,3,10,-4,7,2,-5],最大子数组为[3,10,-4,7,2]，输出18
"""


def max_subarray(array):
    if not isinstance(array, list) or not array:
        return 'Invalid Input'
    max_value = None
    start = None
    # 找到第一个正数作为起点
    for i in range(0, len(array)):
        if array[i] > 0:
            max_value = array[i]
            start = i
            break
    current_value = max_value # 当前子数组的和
    for j in range(start+1, len(array)):
        current_value += array[j]
        current_value = array[j] if current_value < array[j] else current_value # 之前的子数组不合要求,重新选取子数组起点
        max_value = current_value if max_value < current_value else max_value
    return max_value


array = [1, -2, 3, 10, -4, 7, 2, -5]
print(max_subarray(array))
