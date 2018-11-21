# usr/bin/env python
#-*-coding:utf-8-*-

import random
import time


def selectsort(array):
    """每一轮选择出最小的放到头部,减少了比较次数"""
    # 前n-1个数字确定后,第n个数字不用比较
    for i in range(0, len(array) - 1):
        minindex = i
        # 第i个数字即是第i小的，每次从i+1开始比较
        for j in range(i + 1, len(array)):
            if array[minindex] > array[j]:
                minindex = j
        if i != minindex:
                # 交换
            array[i], array[minindex] = array[minindex], array[i]
    return array

array = []
for i in range(0, 10000):
    array.append(random.randint(0, 10000))
start = time.time()
selectsort(array)
print(time.time() - start)
