#! usr/bin/env python
# -*-coding:utf-8 -*-
"""
在一个二维数组中，每一行从左到右递增，每一列从上到下递增，输入一个整数判断是否在该数组内。
思路:从右上角或左下角数字开始比较，相等则退出，不等则比较，每次都会在数组查找范围中删除一行或一列。
"""


def find(dataList, data):
    column = 0
    for row in range(len(dataList)):
        if row == 0:
            column = len(dataList[row])-1 # 记录列数
        while column > 0:
            if dataList[row][column] == data:
                return True
            elif dataList[row][column] > data:
                column -= 1
            elif dataList[row][column] < data:
                break
    return False


if __name__ == '__main__':
    data = int(input("输入查找数字："))
    dataList = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    print(find(dataList, data))
