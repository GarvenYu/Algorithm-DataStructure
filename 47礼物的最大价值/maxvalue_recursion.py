#! usr/bin/env python3
# -*-coding:utf-8-*-

"""
题目：在一个m*n的棋盘上每一格放了一个礼物，每个礼物都有一定的价值(价值大于0)。
你可以从棋盘的左上角开始拿礼物，并每次向右或者向下移动一格，直到到达棋盘右下角。
给定一个棋盘及其上面的礼物，最多能拿到多少价值的礼物？
"""


def max_value_of_gift_recursion(array, rows, cols, row, col) -> int:
    """递归解法"""
    value1 = 0
    value2 = 0
    if row < rows and col < cols:
        value = array[row][col]
        # 向下走
        value1 = max_value_of_gift_recursion(array, rows, cols, row + 1, col) + value
        # 向右走
        value2 = max_value_of_gift_recursion(array, rows, cols, row, col + 1) + value
    return max(value1, value2)


array = [[1, 10, 3, 8], [12, 2, 9, 6], [5, 7, 4, 11], [3, 7, 16, 5]]
rows = len(array)
cols = len(array[0])
print(max_value_of_gift_recursion(array, rows, cols, 0, 0))  # 53
