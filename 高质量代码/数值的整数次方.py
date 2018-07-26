#! usr/bin/env python
# -*-coding:UTF-8 -*-
"""
实现一个函数power(base,exponent),输出base的exponent次方。不使用库函数，不考虑大数问题。
"""


def power(base, exponent):
    """
    :base 基数
    :exponent 幂
    # 注意几种情况：
    # exponent 为正数/负数/0
    # base 为0
    """
    try:
        if exponent == 0:
            result = 1
        if exponent < 0:
            exponent = abs(exponent)
            result = 1/powerCore(base, exponent)
            result2 = 1/powerHighEfficiency(base, exponent)
        else:
            result = powerCore(base, exponent)
            result2 = powerHighEfficiency(base, exponent)
    except Exception as e:
        print(e)
        return 0
    else:
        return result2


def powerCore(base, exponent):
    result = 1
    for idx in range(1, exponent+1):
        result = result * base
    return result


def powerHighEfficiency(base, exponent):
    """高效率解法"""
    if exponent == 1:
        return base
    result = powerHighEfficiency(base, exponent >> 1)  # 除2到底
    result *= result  # 平方
    if exponent & 0x1 == 1:  # 如果是奇数,除2时会余1
        result *= base
    return result


if __name__ == '__main__':
    print(power(5, 100))
