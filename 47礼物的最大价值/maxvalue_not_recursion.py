# !usr/bin/env python3
# -*-coding:UTF-8-*-

"""
非递归解法(需借助辅助空间);
"""


def max_value_not_recursion(array, max_values):
    if not array or not array[0]:
        print('Invalid Input!')
    rows = len(array)
    cols = len(array[0])
    for row in range(0, rows):
        for col in range(0, cols):
            left = 0
            up = 0
            if row > 0:
                # 非第一行
                up = max_values[row - 1][col]
            if col > 0:
                # 非第一列
                left = max_values[row][col - 1]
            # (row,col)的最大值只取决于(row-1,col)上和(row,col-1)左
            max_values[row][col] = max(up, left) + array[row][col]
    return max_values[rows - 1][cols - 1]  # 返回最后一个值


array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
max_values = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(max_value_not_recursion(array, max_values))
