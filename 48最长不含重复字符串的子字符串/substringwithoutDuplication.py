#! usr/bin/env python
# -*-coding:UTF-8-*-

"""
题目：最长不含重复字符的子字符串
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。假设字符串中只包含从’a’到’z’的字符。
示例：在字符串中”arabcacfr”，最长非重复子字符串为”acfr”，长度为4。
"""


def substring_without_duplication(case):
    if not case:
        return 'Invalid Input!'
    else:
        c_length = 0
        m_length = 0
        position = {}
        s_length = len(case)
        for i in range(s_length):
            prev_index = position.get(case[i], -1)
            if prev_index == -1 or i - prev_index > c_length:
                c_length += 1
            else:
                if c_length > m_length:
                    m_length = c_length
                c_length = i - prev_index
            # update position
            position[case[i]] = i
        if c_length > m_length:
            m_length = c_length
        return m_length


testcase = 'arabcacfr'
print(substring_without_duplication(testcase))  # 4
