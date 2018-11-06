# usr/bin/env python
#-*-coding:utf-8-*-

import time
import random


def bubblesort(array):
    """冒泡排序第一版"""
    start = time.time()
    for i in range(len(array), 0, -1):
        for j in range(0, i - 1):
            if array[j] > array[j + 1]:
                # 交换
                array[j + 1], array[j] = array[j], array[j + 1]
    end = time.time()
    print(end - start)
    return array


def bubblesort_fix(array):
    """冒泡排序第二版
    通过记录最后一次发生交换的位置,减少冒泡次数，当数组有序时尤为明显"""
    start = time.time()
    # 最后一次发生交换的位置
    last_pos = len(array)
    for i in range(last_pos, 0, -1):
        # 记录是否发生了交换，否则直接退出，说明此时已有序不需要再冒泡
        flag = True
        for j in range(0, i - 1):
            if array[j] > array[j + 1]:
                array[j + 1], array[j] = array[j], array[j + 1]
                last_pos = j
                flag = False
        if flag:
            end = time.time()
            print(end - start)
            return array

array = []
for times in range(0, 10000):
    # 构造测试数据有序数组
    array.append(random.randint(0, 10000))
bubblesort_fix(array)
bubblesort(array)
