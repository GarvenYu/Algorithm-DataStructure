#! usr/bin/env python3
# -*-coding:utf-8-*-

"""
描述：滑动窗口的最大值
给定一个数组和滑动窗口的大小，找出所有滑动窗口里的最大值。
示例：输入数组[2,3,4,2,6,2,5,1]及滑动窗口的大小3，那么一共存在6个滑动窗口，最大值分别为[4,4,6,6,6,5]
思路：队列先入先出特性的考察
"""


def max_value_in_window(array, window):
    if not array:
        return None
    else:
        task_queue = []  # 存储滑动过程中的最大值
        begin_index = 0
        if len(array) < window:
            #  如果数组长度小于窗口大小
            #  找到数组中的最大元素并输出
            task_queue.append(begin_index)
            while begin_index + 1 < len(array):
                begin_index += 1
                if array[begin_index] > array[task_queue[0]]:
                    task_queue.pop()
                    task_queue.append(begin_index)
                else:
                    pass
            return array[task_queue.pop()]
        else:
            #  如果数组长度大于等于窗口大小
            window_counts = len(array) - window + 1  # 窗口数
            for i in range(0, window_counts):
                task_queue.append(i)
                # 判断窗口队列中的头元素是否不在窗口中需要移除
                if task_queue[0] < i:
                    task_queue.pop(0)
                for j in range(i, i + window):
                    # 在一次窗口遍历中
                    if array[j] > array[task_queue[0]]:
                        task_queue.clear()  # 清空队列
                        task_queue.append(j)
                    else:
                        continue
                print(array[task_queue[0]], end=" ")  # 打印当前窗口最大元素


array = [2, 3, 4, 2, 6, 2, 5, 1]
window = 3
max_value_in_window(array, window)  # 4 4 6 6 6 5
