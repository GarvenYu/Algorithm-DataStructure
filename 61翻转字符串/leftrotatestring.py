#! usr/bin/env python3
# -*-coding:utf-8-*-

"""
描述：左旋转字符串
左旋转操作是指把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。
示例：输入字符串abcdefg和数字2，返回结果cdefgab。
思路：reverse3次
"""


def reverse_word(word, begin, end):
    while begin < end:
        word[begin], word[end] = word[end], word[begin]
        begin += 1
        end -= 1


def left_rotate(sentence, n):
    if not sentence or n > len(sentence):
        print('Invalid Input.')
        return
    else:
        reverse_word(sentence, 0, len(sentence) - 1)  # 整句旋转
        # 以n为分界点分别旋转
        reverse_word(sentence, 0, len(sentence) - n - 1)
        reverse_word(sentence, len(sentence) - n, len(sentence) - 1)
        print(''.join(sentence))


sentence = 'abcdefg'
left_rotate(list(sentence), 6)