#! usr/bin/env python3
# -*-coding:utf-8-*-

"""
用最小堆来解决TopN的问题
"""


class TopN:
    def __init__(self, n, data):
        self.n = n
        self.data = data

    @staticmethod
    def parent(index):
        return (index - 1) // 2

    @staticmethod
    def left(index):
        return 2 * index + 1

    @staticmethod
    def right(index):
        return 2 * index + 2

    def build_heap(self):
        for i in range(self.n):
            t = i
            while self.parent(t) >= 0 and self.data[t] < self.data[self.parent(t)]:
                # 调整堆
                self.data[t], self.data[self.parent(t)] = self.data[self.parent(t)], self.data[t]
                t = self.parent(t)

    def adjust_heap(self, num):
        if num <= self.data[0]:
            return
        # 调整堆
        t = 0
        self.data[t] = num
        while (self.left(t) < self.n and self.data[t] > self.data[self.left(t)]) or \
                (self.right(t) < self.n and self.data[t] > self.data[self.right(t)]):
            # 如果父节点大于左孩子或者右孩子，并且左或右孩子存在
            if self.left(t) < self.n and self.data[t] > self.data[self.left(t)]:
                # 左孩子
                self.data[t], self.data[self.left(t)] = self.data[self.left(t)], self.data[t]
                # 新的顶点和右孩子比较,这一步容易遗漏
                if self.data[t] > self.data[self.right(t)]:
                    self.data[t], self.data[self.right(t)] = self.data[self.right(t)], self.data[t]
                t = self.left(t)
            else:
                self.data[t], self.data[self.right(t)] = self.data[self.right(t)], self.data[t]
                t = self.right(t)

    def find_TopN(self, nums):
        self.build_heap()
        for d in nums:
            self.adjust_heap(d)

    def print_heap(self):
        for d in self.data:
            print(d)


# Test Case
# 假设data是nums的前5个元素，从data+nums中找出Top5
n = 5
data = [5, 4, 3, 2, 1]
top = TopN(n, data)
nums = [6, 7, 8, 9, 10, 11, 22, 23, 24, 25]
top.find_TopN(nums)
top.print_heap()
