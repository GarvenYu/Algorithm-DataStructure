# !usr/bin/env python3
# -*-coding:utf-8-*-

"""
统计一个数字在排序数组中出现的次数。
示例：输入{1,2,3,3,3,4,5}和3，输出3.
"""


def get_first_k(array, k, start, end):
    """利用二分查找找到第一个K"""
    if start > end:
        return 0
    mid = (start + end) // 2
    if k == array[mid]:
        # 如果前一个数比k小证明这是第一个K, 否则继续在前面找
        if mid == 0 or array[mid - 1] < k:
            return mid + 1  # 返回位置从1开始计数
        else:
            end = mid - 1
    else:
        if k < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return get_first_k(array, k, start, end)


def get_last_k(array, k, start, end):
    """利用二分查找找到最后一个K"""
    if start > end:
        return 0
    mid = (start + end) // 2
    if k == array[mid]:
        # 如果后一个数比k大证明这是第一个K, 否则继续在后面找
        if mid == len(array) - 1 or array[mid + 1] > k:
            return mid + 1  # 返回位置从1开始计数
        else:
            start = mid + 1
    else:
        if k < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return get_last_k(array, k, start, end)


def get_k_counts(array, k):
    """输出K出现的次数"""
    if not array:
        return 0
    first = get_first_k(array, k, 0, len(array) - 1)
    last = get_last_k(array, k, 0, len(array) - 1)
    if first and last:
        return last - first + 1
    else:
        return 0


testarray = [1, 2, 3, 3, 3, 4, 5]
print(get_k_counts(testarray, 3))
