#! usr/bin/env python
# -*-coding:utf-8 -*-

"""
一个m行n列的方格，机器人从(0,0)开始运动，每次可以向左、右、上、下移动一格，但不能进入行坐标和列坐标的数位之和大于K的格子。
判断最多能到达多少个格子
"""


def countMotion(rows, cols, key):
    """
    :param rows:行
    :param cols:列
    :param key:阈值
    """
    if rows <= 0 or cols <= 0 or key < 0:
        return 0
    # 布尔值矩阵,标识路径是否已经进入了某个格子
    visited = []
    for row in range(rows):
        visited.append([])
        for col in range(cols):
            visited[row].append(0)
    motion = 0
    row = 0
    col = 0
    motion = countMotionCore(rows, cols, key, visited, motion, row, col)
    return motion


def countMotionCore(rows, cols, key, visited, motion, row, col):
    if row >= 0 and row < rows and col >= 0 and col < cols and not visited[row][col]:
        if check(row, col, key):
            visited[row][col] = 1
            motion = 1 + \
            countMotionCore(rows, cols, key, visited, motion, row, col-1) + \
            countMotionCore(rows, cols, key, visited, motion, row, col+1) + \
            countMotionCore(rows, cols, key, visited, motion, row-1, col) + \
            countMotionCore(rows, cols, key, visited, motion, row+1, col)
    return motion

def check(row, col, key):
    """
    判断数位相加是否<=阈值,(12,12) = 1+2+1+2 = 6
    """
    indexSum = 0
    row_number = row
    col_number = col
    while row_number // 10 >= 10:
        indexSum += row_number % 10
        row_number = row_number // 10
    indexSum += (row_number // 10) + (row_number % 10)
    while col_number // 10 >= 10:
        indexSum += col_number % 10
        col_number = col_number // 10
    indexSum += (col_number // 10) + (col_number % 10)
    return indexSum <= key


if __name__ == '__main__':
    print(countMotion(1, 2, 1))
