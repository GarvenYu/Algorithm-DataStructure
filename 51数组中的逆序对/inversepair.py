#! usr/bin/env python3
# -*-coding:utf-8-*-

"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数。
示例：数组{7,5,6,4}，逆序对总共有5对，{7,5}，{7,6}，{7,4}，{5,4}，{6,4}；
解法：
1.蛮力法，对于第i个字符，向后遍历n-i次，复杂度O(n^2);
2.分治法，基于归并排序的思路，时间复杂度O(nlogn)，空间复杂度O(n)，注意排序中间结果集
"""


def stat_inverse_pair_core(array):
    global count
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = stat_inverse_pair_core(array[:mid])
    right = stat_inverse_pair_core(array[mid:])
    left_index = len(left) - 1  # 从后向前遍历检查逆序对
    right_index = len(right) - 1
    result = [None] * (len(left) + len(right))
    while left_index >= 0 and right_index >= 0:
        if left[left_index] > right[right_index]:
            # 逆序对等于此时right数组从0到right_index的个数
            count += len(right[:right_index]) + 1  # 包括right_index自己
            result[left_index + right_index + 1] = left[left_index]  # 大元素copy到结果集最后一位
            left_index -= 1
        else:
            result[left_index + right_index + 1] = right[right_index]  # 大元素copy到结果集最后一位
            right_index -= 1
    # 剩余部分copy到result中
    if left_index < 0:
        # left数组遍历完
        for i in range(0, right_index + 1):
            result[i] = right[i]
    else:
        # right数组遍历完
        for i in range(0, left_index + 1):
            result[i] = left[i]
    return result


array = [7, 5, 6, 4]
count = 0
stat_inverse_pair_core(array)
print(count)  # output = 5
