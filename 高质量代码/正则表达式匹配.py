#! usr/bin/env python
# -*-coding:UTF-8 -*-
"""
实现一个函数用来匹配包含'.'和'*'的正则表达式。'.'表示任一字符，'*'表示前一个字符出现0或多次。
"""


def matchRegex(string, pattern):
    if not string or not pattern:
        return False
    return matchRegexCore(string, pattern)


def matchRegexCore(string, pattern):
    if not string and not pattern:
        return True
    if not string or not pattern:
        return False	
    if pattern[1] == '*':
        if string[0] == pattern[0] or (pattern[0] == '.' and string):
            return matchRegexCore(string[1:], pattern) \
                or matchRegexCore(string[1:], pattern[2:]) \
                or matchRegexCore(string, pattern[2:])
        else: 
            return matchRegexCore(string, pattern[2:])
    if string[0] == pattern[0] or (pattern[0] == '.' and string):
        return matchRegexCore(string[1:], pattern[1:])
    return False  # 其余情况都视为不匹配


if __name__ == '__main__':
    string = 'acb'
    pattern = '.*xc.*'
    print(matchRegex(string, pattern))
