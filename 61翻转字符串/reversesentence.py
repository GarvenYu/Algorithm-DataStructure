#! usr/bin/env python3
# -*-coding:utf-8-*-

"""
描述：翻转单词顺序
输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变，标点符号和普通字母一样处理。
示例：输入"I am a student." 输出"student. a am I"
思路：第一步翻转句子中所有字符；第二步再翻转每个单词中字符的顺序
"""


def reverse_sentence(sentence):
    if not sentence:
        print('Invalid Input Data')
        return
    reverse_word(sentence, 0, len(sentence) - 1)
    # 再翻转单个单词
    begin = 0
    end = 0
    while end < len(sentence):
        if sentence[end] == ' ':
            # 如果遇到分隔符，进行翻转
            reverse_word(sentence, begin, end - 1)
            end += 1
            begin = end
        elif end == len(sentence) - 1:
            # 如果到最后一个字符，此时没有分隔符，依然需要翻转
            reverse_word(sentence, begin, end)
            end += 1
        else:
            end += 1
    print(''.join(sentence))


def reverse_word(word, begin, end):
    while begin < end:
        word[begin], word[end] = word[end], word[begin]
        begin += 1
        end -= 1


sentence = 'I am a student.'
reverse_sentence(list(sentence))
