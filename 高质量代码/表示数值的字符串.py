#! usr/bin/env python
# -*-coding:utf-8-*-

"""
实现一个函数判断字符串是否表示数值（包括整数和小数）
例如+100,5e2，-123,3.14，-1E-16都表示数值，但12e，1a3.14,1.2.3，+-5,12e+5.4都不是。
"""


def is_number(string):
    if not string:
        return False
    return is_number_core(string, len(string))


def is_number_core(string, str_len):
    """符合要求的数据组成格式：(有符号数)(.)(无符号数)(e|E)(有符号数)"""
    index = 0
    # 第一部分是否是有符号数
    is_number = is_integer(string, index, str_len)
    if index != str_len:
        if string[index] == '.':
            # 第二部分是否是无符号数
            # .123 = 0.123
            # 12. = 12.0
            index += 1
            is_number = is_unsigned_integer(
                string, index, str_len) or is_number
    if index != str_len:
        if string[index] in ('e', 'E',):
            # 第三部分是否是有符号数且e|E前面必须有数字,此部分不可省略
            index += 1
            is_number = is_integer(string, index, str_len) and is_number
    return is_number and (index == str_len)


def is_integer(string, index, str_len):
    """判断是否是有符号整数"""
    if string[index] in ('+', '-'):
        index += 1
    return is_unsigned_integer(string, index, str_len)


def is_unsigned_integer(string, index, str_len):
    """判断是否是无符号整数"""
    before = index
    for i in range(index, str_len):
        if '0' <= string[i] <= '9':
            index += 1
    return before != index

if __name__ == '__main__':
    string = '+123'
    print(is_number(string))
