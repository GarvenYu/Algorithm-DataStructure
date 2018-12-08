#! usr/bin/env python
# -*-coding:UTF-8-*-

"""
题目：最长不含重复字符的子字符串
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。假设字符串中只包含从’a’到’z’的字符。
示例：在字符串中”arabcacfr”，最长非重复子字符串为”acfr”，长度为4。
"""


def substring_without_duplication(string):
    if not string:
        return 'Invalid Input!'
    else:
        position = []
        result = [0, '']  # 存储最终结果,result[0]=maxlength,result[1]=maxsubstring
        for i in range(0, 26):
            position.append(-1)  # 初始化位置数组，26个字母对应26个位置
        for start in range(0, len(string)):
            move = 0  # 记录移动步数
            while (start + move < len(string)):
                curword = string[start + move]
                if (start + move) - position[ord(curword) - ord('a')] > move or move == 0:
                    # 如果是新一轮的第一个字符或者当前字符上一次出现的位置不在本次遍历中
                    if result[0] < move + 1:
                        #  更新最长子字符串
                        result[0] = move + 1
                        result[1] = string[start:start + move + 1]
                    # 更新当前字符最新出现的位置
                    position[ord(string[start + move]) - ord('a')] = start + move
                    move += 1
                else:
                    # 当前字符在当前子字符串中重复出现
                    break
        return result


string = 'arabacfr'
print(substring_without_duplication(string))
