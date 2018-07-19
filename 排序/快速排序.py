#!usr/bin/env/ python
#-*-coding:utf-8-*-
import random


def swap(data, randIndex, end):
    tmp = data[randIndex]
    data[randIndex] = data[end]
    data[end] = tmp


def partition(data, start, end, length):
    if not data:
        return "Invalid Data"
    if not isinstance(start, int) or not isinstance(end, int) or not isinstance(length, int):
        return "Invalid parameter"
    if start < 0 or end > (length - 1):
        return "Error parameter"
    # 区间内随机取哨兵, start<=randIndex<=end
    randIndex = random.randint(start, end)
    # 交换
    swap(data, randIndex, end)
    print(data)
    print(str(start) + '->' + str(end))
    pivot = start - 1
    for index in range(start, end):
        if data[index] < data[end]:
            pivot += 1
            if pivot != index:
                swap(data, pivot, index)
    pivot += 1
    swap(data, pivot, end)
    return pivot


def quickSort(data, start, end):
    """快速排序"""
    pivot = partition(data, start, end, len(data))
    if start < pivot:
        quickSort(data, start, pivot - 1)
    if pivot < end:
        quickSort(data, pivot + 1, end)
    return data


if __name__ == '__main__':
    data = [5, 3, 2, 7, 4, 1, 8, 9]
    print(quickSort(data, 0, len(data) - 1))
