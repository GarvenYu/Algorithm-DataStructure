#! usr/bin/env python
# -*-coding:utf-8 -*-
"""
有两个排序的数组A和B，内存在A的末尾有足够空间容纳B，请实现把B中所有数字插入A中，并且所有数字是有序的。
思路:从后向前比较AB中的数字，把较大的数字复制到A中(从前向后会出现多次复制同一个数字来空出位置,时间复杂度高)
"""
import pdb


def merge(a, b):
    if not a:
        return b
    if not b:
        return a
    resultLength = len(a) + len(b)
    result = [None]*(resultLength)
    aLast = len(a)-1
    bLast = len(b)-1

    while resultLength >= 0 and bLast >= 0 and aLast >= 0:
        '''
        合并list直到某一个list遍历完毕
        '''
        if b[bLast] >= a[aLast]:
            result[resultLength-1] = b[bLast]
            resultLength -= 1
            bLast -= 1
        elif b[bLast] < a[aLast]:
            result[resultLength-1] = a[aLast]
            resultLength -= 1
            aLast -= 1

    while aLast < 0 and bLast >= 0:
        '''
        将另一个没有遍历完的集合插入结果集
        '''
        result[resultLength-1] = b[bLast]
        resultLength -= 1
        bLast -= 1

    while bLast < 0 and aLast >= 0:
        result[resultLength-1] = a[aLast]
        resultLength -= 1
        aLast -= 1
    return result


if __name__ == '__main__':
    a = [2, 3, 4, 5]
    b = [2, 3, 4, 5]
    print(merge(a, b))
