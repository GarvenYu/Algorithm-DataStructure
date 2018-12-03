#! usr/bin/env python3
# -*-coding:utf-8-*-

"""
题目：给定一个数字，有规则如下，"0"翻译成"a"，"1"翻译成"b"，...，25翻译成"z"。一个数字可能有多个翻译，实现一个函数，
计算一个数字有多少种不同的翻译方法。
示例：12258有5种不同的翻译，分别是"bccfi","bwfi","bczi","mcfi","mzi"。
思路：两两组合，满足范围要求，则从两位数字后进行递归，每有一个两位组合就有一个方法，result += 1。
"""


def cast_number_to_string(number, start_index, result):
    if not number:
        return 'Invalid Input'
    while(start_index > 0):
        if '10' <= number[start_index-1] + number[start_index] <= '25':
            result += 1
            result = cast_number_to_string(number, start_index - 2, result)
        start_index -= 1
    return result


number = '12258'
start_index = len(number) - 1
result = 1  # 至少有一种组合方式即全分散组合
print(cast_number_to_string(number, start_index, result))