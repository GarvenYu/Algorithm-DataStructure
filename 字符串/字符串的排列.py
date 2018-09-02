#! usr/bin/env python
#-*-coding:utf-8-*-

"""
输入一个字符串，打印出该字符串中字符的所有排列。例如，输入abc，则打印出abc,acb,bac,bca,cab,cba
第一步：求所有可能出现在第一个位置的字符；
第二步：固定第一个字符,求后面字符串的排列(重复1/2步)；
递归。
"""


def permutation(print_str):
    if not print_str:
        print("")
        return
    else:
        index = 0
        permutation_core(print_str, index, print_str)


def swap(data_list, index1, index2):
    data_list[index1], data_list[index2] = data_list[index2], data_list[index1]


def permutation_core(print_str, index, sub_str):
    if index == len(print_str) - 1:
        # 遍历到最后一个字符
        # 输出
        print(print_str)
    else:
        for i in range(0, len(sub_str)):
            index = index + 1
            permutation_core(print_str, index, sub_str[index:])
            swap(print_str, index, i)
            index -= 1


if __name__ == '__main__':
    print_str = ['a', 'b', 'c']
    permutation(print_str)
