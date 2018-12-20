# !usr/bin/env python3
# -*-coding:utf-8-*-

"""
描述：输入一个正数s，打印出所有和为s的连续正数序列（至少含有两个数）。
示例：输入15，由于1+2+3+4+5=4+5+6=7+8=15，打印3个连续序列1-5,4-6,7-8。
"""

def find_sequence(s):
    if s <= 0:
        return None
    else:
        result = [1,2]
        small = 0 # 指向头
        big = 1 # 指向尾
        current_sum = 3 # sum from small to big
        find = False
        while small < (s // 2):          
            if current_sum == s:
                find = True
                print(result[small : big+1])
                # big右移，新加一个数字
                result.append(result[big] + 1)
                big += 1
                current_sum += result[big]
            elif current_sum < s:
                # big右移，新加一个数字
                current_sum += result[big] + 1
                result.append(result[big] + 1)
                big += 1                
            else:
                # small右移
                current_sum -= result[small]
                small += 1
        if not find:
            print('No Match Data')


find_sequence(10)
