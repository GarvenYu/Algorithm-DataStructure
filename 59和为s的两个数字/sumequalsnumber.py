# !usr/bin/env python3
# -*-coding:utf-8-*-

"""
描述：输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，输出任意一对。
示例：输入[1, 2, 4, 7, 11, 15]和数字15，输出(4,11)
思路：定义头尾两个指针t1和t2，如果t1 + t2 > s,t2--；如果t1 + t2 < s,t1++
"""

def find_numbers_sum_s(array, s):
    if not array or len(array) == 1:
        return None, None
    else:
        head = 0
        tail = len(array) - 1
        while head != tail:
            if s == (array[head] + array[tail]):
                return array[head], array[tail]
            elif s > (array[head] + array[tail]):
                head += 1
            else:
                tail -= 1              
        # 没找到
        return None, None

    
array = [1, 2, 4, 7, 11, 15]
s = 15
print(find_numbers_sum_s(array, s))