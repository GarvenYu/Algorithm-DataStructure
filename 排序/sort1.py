# usr/bin/env python
# -*-coding:utf-8-*-


def bubbleSort(array):
    """冒泡排序"""
    if not array:
        return None
    else:
        for i in range(0, len(array)):
            flag = False
            for j in range(0, len(array) - i - 1):
                if array[j] > array[j + 1]:
                    # 交换
                    # 与插入排序相比，有3次原子操作
                    array[j], array[j + 1] = array[j + 1], array[j]
                    flag = True
            if not flag:
                break
        return array


def insertSort(array):
    """插入排序"""
    if not array:
        return None
    else:
        for i in range(1, len(array)):
            value = array[i]
            j = i - 1
            while j >= 0 and array[j] > value:
                # 大元素后移
                # 与冒泡排序相比，这里只有1次原子操作
                array[j + 1] = array[j]
                j -= 1
            # 插入元素
            array[j + 1] = value
        return array


def selectSort(array):
    """选择排序"""
    if not array:
        return None
    else:
        for i in range(0, len(array) - 1):
            min_index = i
            for j in range(i + 1, len(array)):
                if array[min_index] > array[j]:
                    min_index = j
            if min_index != i:
                array[i], array[min_index] = array[min_index], array[i]
        return array
