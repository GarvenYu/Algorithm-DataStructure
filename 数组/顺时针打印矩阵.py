#！usr/bin/env python
#-*-coding:utf-8-*-

"""
输入一个矩阵,按照从外向里以顺时针的顺序依次打印出每一个数字。
"""


def print_matrix_circle(matrix, rows=0, cols=0, start_row=0, start_col=0, visit_flag=False):
    if not matrix:
        return None
    else:
        for col in range(start_col, cols):
            # 向右输出
            print(matrix[start_row][col])
        for row in range(start_row + 1, rows):
            # 向下输出
            print(matrix[row][cols - 1])
        for col2 in range(cols - 1 - 1, start_col - 1, -1):
            if rows - 1 != start_row:
                # 非单行情况
                # 向左输出
                print(matrix[rows - 1][col2])
        for row2 in range(rows - 1 - 1, start_row, -1):
            if cols - 1 != start_col:
                # 非单列情况
                # 向上输出
                print(matrix[row2][start_col])
                # 防止递归溢出
                visit_flag = True
        if visit_flag:
            print_matrix_circle(matrix, rows - 1, cols - 1,
                                start_row + 1, start_col + 1)

if __name__ == '__main__':
    matrix1 = [[1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [
        1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]]  # 多行多列
    matrix2 = [[1, 2, 3]]  # 只有一行
    matrix3 = [[1], [4], [7]]  # 只有一列
    print_matrix_circle(matrix1, rows=8, cols=7)
