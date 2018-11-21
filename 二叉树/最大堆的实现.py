# usr/bin/env python
# -*-coding:utf-8-*-

# 由于堆是完全二叉树，所以父节点n的两个子节点分别是2n+1，2n+2；
# 最后一个父节点的位置是 len(heap)//2 - 1；
# 当前节点i的父节点为 (i - 1) // 2;


class MaxHeap(object):

    def __init__(self, data=[]):
        self._array = data
        self.build_max_heap()

    def __len__(self):
        return len(self._array)

    def __repr__(self):
        return self._array

    def swap(self, x, y):
        """交换元素
        """
        self._array[x], self._array[y] = self._array[y], self._array[x]

    def build_max_heap(self):
        """构造最大堆
        """
        pass

    def float_up(self, index):
        """如果index位置的元素>父节点元素，那么上浮
        """
        pass

    def float_down(self, index):
        """如果index位置的元素<左或右孩子节点，那么下沉
        """
        pass

    def append(self, data):
        """向堆尾动态添加元素
        """
        self._array.append(data)
        self.float_up(len(self) - 1)  # 叶子节点上浮

    def pop(self):
        """堆中头元素出列
        """
        self.swap(0, len(self) - 1)  # 交换头尾元素
        item = self._array.pop(len(self) - 1)  # 尾元素出列
        self.float_down(0)  # 头元素下沉
        return item
