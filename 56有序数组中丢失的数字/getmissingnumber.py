# !usr/bin/env python3
# -*-coding:utf-8-*-

"""
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0~n-1之内。在范围0~n-1之内的
n个数字中有且只有一个数字不在该数组中，请找出这个数字。
思路：范围内每个数字都跟数组下标相等，假设缺失的数字是m，小于m的数字都跟下标对应，大于m的数字发生错位，所以只需要找到第一个值和下标不相等的元素。
"""


def get_missing_number(array, n):
    start = 0
    end = n
    while start < end:
        mid = (end+start) >> 1
        if array[mid] == mid:
            # 右边找
            start = mid +1
        else:
            # 如果前一个数字值与下标相等或此时mid=0
            if mid - 1 == array[mid - 1] or mid == 0:
                return mid # 返回此时的下标
            else:
                # 左边找
                end = mid - 1
    return n # 丢失了最后一个元素,array内所有元素都和下标相等


array = [0,1,2,3,4,5,6,8]
print(get_missing_number(array, 8)) # 7