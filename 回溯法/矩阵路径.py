#! usr/bin/env python
# -*-conding:utf-8-*-


def haveRoute(matrix,rows, cols, route):
    """
    :param matrix:矩阵
    :param rows:总行数
    :param cols:总列数
    :param route:字符串
    :return bool
    """
    if not matrix or not route:
        return False
    visited = []
    for row in range(len(matrix)):
        visited.append([])
        for col in range(len(matrix[row])):
            visited[row].append(0)
    # index = 0
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            if haveRouteCore(route, visited, matrix, row, col, rows, cols):
                return True
    return False


def haveRouteCore(route, visited, matrix, row, col, rows, cols, index=0):
    haveRoute = False
    if index == len(route):
        return True
    if 0 <= row < rows and 0 <= col < cols and matrix[row][col] == route[index] \
            and visited[row][col] == 0:
        # 当前矩阵的元素 = 字符串相应位置的元素
        # 当前行不能为负数也不能超过总行数
        # 当前列不能为负数也不能超过总列数
        # 不能重复进入
        index += 1
        visited[row][col] = 1
        haveRoute = haveRouteCore(route, visited, matrix, row-1, col, rows, cols, index) or \
            haveRouteCore(route, visited, matrix, row, col-1, rows, cols, index) or \
            haveRouteCore(route, visited, matrix, row+1, col, rows, cols, index) or \
            haveRouteCore(route, visited, matrix, row,
                          col+1, rows, cols, index)
        if not haveRoute:
            index -= 1
            visited[row][col] = 0
    return haveRoute


if __name__ == '__main__':
    matrix = [['a', 'b', 'c', 'd'], ['q', 'w', 'e', 'r'], ['t', 'y', 'u', 'i']]
    data = 'aqtyweuir'
    if haveRoute(matrix, len(matrix), len(matrix[0]), data):
        print('有此路径 %s' % data)
    else:
        print('无此路径 %s' % data)