#! usr/bin/env python
#-*-coding:utf-8-*-

"""
输入一个递增排序的数组的一个旋转,输出旋转数组的最小元素。
"""


def min_data(data):
    """
    输出旋转数组的最小元素
    """
    if not data:
        return "Invalid Data"
    # 特殊情况：
    # 旋转数组是排序数组自身(取0个元素放到后面)
    head = 0
    foot = len(data)-1
    if data[head] < data[foot]:
        return data[head]
    else:
        # 当头指针和尾指针还没相邻时
        while foot - head > 1:
            mid = (foot+head)//2

            # 如果重复元素过多,导致data[head]=data[mid]=data[foot]
            # 从头顺序遍历输出
            if data[head] == data[mid] == data[foot]:
                return go_through_in_order(data)

            if data[mid] >= data[head]:
                # 最小元素在mid后面
                head = mid
            elif data[mid] <= data[foot]:
                # 最小元素在mid前面
                foot = mid
        # 有序的旋转数组小元素在后面
        return data[foot]


def go_through_in_order(data):
    min_data = data[0]
    for index in range(1, len(data)):
        if data[index] < min_data:
            min_data = data[index]
    return min_data


if __name__ == '__main__':
    data = [1, 0, 1, 1, 1]
    print(min_data(data))
