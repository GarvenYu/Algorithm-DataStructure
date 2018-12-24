# !usr/bin/env python3
# -*-coding:utf-8-*-

"""
描述：把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。
思路：递归解法，构造临时数组存储每种结果能出现的次数，找到结果在临时数组中应该存放的位置，使次数+1。
第一个骰子1对应1+(1/2/3/4/5/6),2对应2+(1/2/3/4/5/6)...
"""


def print_probability(n):
    if not n:
        print('Invalid Input')
    else:
        result = [0] * (5*n+1) # 初始化,记录每种结果出现的次数，共5n+1种情况
        origin = n  # 记录原始的n
        result = print_probability_core(n, result, origin)
        for i in range(0, len(result)):
            print('数字%d出现的概率是%.3f' % (i + n, result[i] / 6**n))


def print_probability_core(n, array, origin, tmp=0):
    if n == 0:
        array[tmp - origin] += 1  # 相应位置增加出现次数
    else:
        for i in range(1, 7):  # 代表初始点数1-6
            tmp += i  # 中间结果
            array = print_probability_core(n - 1, array, origin, tmp)
            tmp -= i
    return array


n = 2
print_probability(n)