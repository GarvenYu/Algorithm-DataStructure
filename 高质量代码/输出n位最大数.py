#! usr/bin/env python
# -*-coding:utf-8-*-

"""
输入数字n，按顺序打印出从1到最大的n位十进制数。比如n=3，则打印1,2,3...999。
大数问题，使用字符串或数组来表达大数。
每次自增后快速判断是否达到了最大的n位数。
"""


def increment(result, n):
    """
    :function 非递归模拟自然数自增解法
    :result 结果数组
    :n 输入的位数
    """
    nOverFlow = False
    nCarry = 0
    for i in range(n - 1, -1, -1):  # start end step
        if nCarry == 1 and i == 0 and result[i] == 9:
            nOverFlow = True
            return nOverFlow
        if result[i] == 9:
            nCarry = 1
            result[i] = 0
            continue
        result[i] += 1
        break
    return nOverFlow


def permutation(result, n, index):
    """
    :function 全排列解法
    :result 同上
    :n 同上
    :index 标识n位数字的每一位
    """
    for i in range(0, 10):
        if index == n - 1:
            result[index] = i
            printResult(result, n)
        else:
            result[index] = i
            permutation(result, n, index + 1)


def printResult(result, n):
    """
    :function 打印结果
    :result 结果数组
    :n 输入的位数
    """
    sResult = ''
    beginPrint = False
    for i in range(0, n):
        if result[i] == 0 and not beginPrint:
            continue
        elif result[i] != 0 or beginPrint:
            sResult += str(result[i])
            beginPrint = True
    print(sResult)


if __name__ == '__main__':
    n = int(input("输入数字n:"))
    result = [0] * n
    # 解法1
    # while not increment(result, n):
    #     printResult(result, n)
    # 解法2
    # permutation(result, n, 0)
