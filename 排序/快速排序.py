#!usr/bin/env/ python
#-*-coding:utf-8-*-
import random


def swap(data, randIndex, end):
    """交换元素"""
    data[randIndex], data[end] = data[end], data[randIndex]


def partition(data, start, end, length):
    """将某个元素放到合适位置并对数组进行分割(左小右大)"""
    if not data:
        return "Invalid Data"
    if not isinstance(start, int) or not isinstance(end, int) or not isinstance(length, int):
        return "Invalid parameter"
    if start < 0 or end > (length - 1):
        return "Error parameter"
    # 区间内随机取哨兵, start<=randIndex<=end
    randIndex = random.randint(start, end)
    # 交换 随机元素放到末尾
    swap(data, randIndex, end)
    pivot = start - 1
    for index in range(start, end):
        if data[index] < data[end]:
            pivot += 1
            if pivot != index:
                # 把大元素换到后面
                swap(data, pivot, index)
    # 哨兵指向比随机元素大的元素
    pivot += 1
    # 进行交换,此时 小 随机元素 大
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
