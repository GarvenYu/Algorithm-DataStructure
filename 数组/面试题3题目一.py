#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
在一个长度为n的数组里的所有数字都是在0~n-1的范围内
'''

data_list = [2, 3, 1, 2, 4, 5, 6]


def find_data(data_list):
    if not data_list:
        return False
    for i in range(len(data_list)):
        while data_list[i] != i:  # 第i个位置的数字必须是i或者为空
            if data_list[i] == data_list[data_list[i]]:
                # 找到重复数字
                print("重复数字 %d" % (int(data_list[i])))
                break
            # 否则进行交换,使data[i]占据第i个位置
            # data_list[i], data_list[data_list[i]] = data_list[data_list[i]], data_list[i]
            temp = data_list[i]
            data_list[i] = data_list[temp]
            data_list[temp] = temp


if __name__ == '__main__':
    find_data(data_list)
