#! usr/bin/env python3
# -*-coding:utf-8-*-

"""
题目：我们把只包含因子2、3、5的数称为丑数。求按从小到大的顺序的第1500个丑数。
示例：4、6、8都是丑数，但14不是，因为它包含因子7.习惯上我们把1当做成第一个丑数。
方法2：空间换时间，降低时间消耗，只判断丑数。
思路：
假设数组中已经有若干个丑数排好序后存放在数组中，并且把已有最大的丑数记为M。因为已有的丑数都是排好序的，
对于乘2而言肯定存在一个丑数位置index2，排在它前面的每一个丑数乘以2得到的结果都会小于已有的最大丑数，
排在它之后的每一个丑数乘以2得到的结果都会太大。(临界点位置)
我们记下index2就可以了，同时每次生成新的丑数的时候，去更新这个index2。对于乘以3、5都一样，分别记录index3和index5.
"""


def get_ugly_number(index):
    if index <= 0:
        return 'Invalid Input!'
    else:
        if index == 1:
            return 1
        else:
            # 丑数数组
            array = [1]
            # 对应因子2，3，5的索引，用来判断下一个丑数该用谁做因子与生成的丑数相乘，来保证生成的是最合适的丑数
            # 初始化都在起点0
            index2 = 0
            index3 = 0
            index5 = 0
            while len(array) < index:
                next_number = min(2 * array[index2], 3 * array[index3], 5 * array[index5])
                if next_number > array[-1]:
                    # 只有比当前最大的丑数大才添加,避免相等的丑数重复添加
                    array.append(next_number)
                while True:
                    if next_number == 2 * array[index2]:
                        index2 += 1
                        break
                    elif next_number == 3 * array[index3]:
                        index3 += 1
                        break
                    elif next_number == 5 * array[index5]:
                        index5 += 1
                        break
            return array[-1]


print(get_ugly_number(1500))
