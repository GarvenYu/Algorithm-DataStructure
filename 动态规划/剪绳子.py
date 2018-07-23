#!usr/bin/env python
# -*- coding: UTF-8 -*-

"""
一根长度为n的绳子,剪成m段,(n>1 m>1),每根绳子长度可能的最大乘积是多少？
"""


def maxCount(length):
    """求剪绳子后最大乘积长度"""
    if length < 2:
        return 0
    elif length == 2:
        return 1
    elif length == 3:
        return 2
    else:
        record = [None] * (length+1)
        # 当剪绳子剩下的长度为0/1/2/3时,可贡献的乘积分别是0/1/2/3
        # 例如length=5,maxCount = 2*3 = 6
        record[0] = 0
        record[1] = 1
        record[2] = 2
        record[3] = 3
        maxCount = 0
        for i in range(4, length+1):
            # 从长度为4开始
            for j in range(1, i//2+1):
                # 若绳子长度为9 
                # j∈[1,4],即长为9的绳子几种剪法对应的乘积分别是
                # record[1]*record[8] record[2]*record[7] record[3]*record[6] record[4]*record[5]
                count = record[j] * record[i-j]
                if count > maxCount:
                    maxCount = count
            # 记录当前长度的最大乘积
            record[i] = maxCount
        return maxCount


if __name__ == '__main__':
    length = 11
    print(maxCount(length)) # 54
