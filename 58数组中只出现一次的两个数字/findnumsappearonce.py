# !usr/bin/env python
# -*-coding:utf-8-*-

"""
一个整型数组里除2个数字外，其他数字都出现了2次。请找出这2个只出现1次的数字。
要求：时间复杂度O(n),空间复杂度O(1)。
示例：数组{2,4,3,6,3,2,5,5},输出4和6。
思路：
1.相同数字进行异或结果为0；
2.从头到尾异或数组中每个数字，得到的结果是数组中只出现1次的两个数字的异或结果，在结果数字中
找到第一个为1的位置，记为第n位。以第n位是否为1将数组分成两部分，这样两个子数组中第n位分别为0和1，
而且每个子数组都包含一个只出现一次的数字，再进行异或输出最后结果。
"""


def array_xor(array):
    i = 0
    result = array[i]
    while i < len(array) - 1:
        result ^= array[i + 1]
        i += 1
    return result


def find_first_bit_1(number):
    """找到右边第一个为1的位置
    """
    index = 0
    while number & 1 == 0:
        number = number >> 1
        index += 1
    return index


def is_bit_1(number, n):
    """判断第n位是否为1
    """
    number = number >> n
    return number & 1


def find_two_numbers(array):
    xor_result = array_xor(array)
    index = find_first_bit_1(xor_result)
    result1 = result2 = 0
    for i in range(0, len(array)):
        if is_bit_1(array[i], index):
            result1 ^= array[i]
        else:
            result2 ^= array[i]
    return result1, result2


array = [2, 4, 3, 6, 3, 2, 5, 5]
print(find_two_numbers(array))
