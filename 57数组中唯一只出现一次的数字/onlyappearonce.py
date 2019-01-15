# !usr/bin/env python3
# -*-coding:utf-8-*-

"""
描述：在一个数组中除一个数字只出现1次之外，其他数字都出现了3次。请找出只出现1次的数字。
思路：如果一个数字出现三次，那么它的二进制表示的每一位(0或1)也出现三次。所有出现三次
的数字，二进制每位进行相加，每一位的和都可以被3整除。
把数组中每个数字的二进制表示按位相加。如果某一位的和能被3整除，那么只出现一次的数字n它的这一位就是0，反之为1。
"""


def only_appear_once_number(array):
    if not array:
        return None
    else:
        bitsum_array = [0] * 32
        for i in range(0, len(array)):
            # array中每个数字都遍历
            for j in range(31, -1, -1):
                # 假设这个数字是int类型，共32位
                if array[i] & 1:
                    # 末位为1
                    bitsum_array[j] += 1
                # 右移1位
                array[i] >>= 1
        result = 0
        # 遍历bitsum数组
        for bit in range(0, 32):
            result <<= 1
            result += bitsum_array[bit] % 3
        return result


array = [1, 1, 1, 2, 2, 2, 5, 6, 6, 6]
print(only_appear_once_number(array))  # 5
