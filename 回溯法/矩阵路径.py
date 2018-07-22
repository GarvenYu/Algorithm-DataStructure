#! usr/bin/env python
# -*-coding:utf-8 -*-

"""
判断在一个矩阵中是否存在一条包含某字符串的路径。
路径可以从矩阵中的任意一格开始；不能重复进入。
"""


def hasPath(matrix, rows, cols, data):
    """
    :param matrix:矩阵
    :param rows:总行数
    :param cols:总列数
    :param data:字符串
    :return bool
    """
    if not matrix or rows <= 0 or cols <= 0 or not data:
        return False
    # 布尔值矩阵,标识路径是否已经进入了某个格子
    visited = []
    for row in range(rows):
        visited.append([])
        for col in range(cols):
            visited[row].append(0)
    index = 0  # data的首字符
    for row in range(rows):
        for col in range(cols):
            # 定位起点
            if hasPathCore(matrix, rows, cols, data, index, visited, row, col):
                return True
    return False


def hasPathCore(matrix, rows, cols, data, index, visited, row, col):
    """
    判断是否存在路径
    """
    if data[index] == '\0':
        return True
    hasPath = False
    if row >= 0 and row < rows and col >= 0 and col < cols and data[index] == matrix[row][col] \
             and not visited[row][col]:
        # 当前矩阵的元素 = 字符串相应位置的元素
        # 当前行不能为负数也不能超过总行数
        # 当前列不能为负数也不能超过总列数
        # 不能重复进入
        visited[row][col] = 1  # 在当前回溯路径中已访问
        index += 1
        hasPath = hasPathCore(matrix, rows, cols, data,index, visited, row, col-1) \
        or hasPathCore(matrix, rows, cols, data, index, visited, row, col+1) \
        or hasPathCore(matrix, rows, cols, data, index, visited, row-1, col) \
        or hasPathCore(matrix, rows, cols, data, index, visited, row+1, col)
        if not hasPath:
            # 撤销赋值操作回溯
            index -= 1
            visited[row][col] = 0
    return hasPath


if __name__ == '__main__':
    matrix = [['a','b','c','d'], ['q','w','e','r'], ['t','y','u','i']]
    data = 'aqtyweuir\0'
    if hasPath(matrix, len(matrix), len(matrix[0]), data):
        print('有此路径 %s' % data)
    else:
        print('无此路径 %s' % data)
