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
        if not self._array:
            return self._array
        # 从最后一个非叶子节点开始，逐个下沉
        for i in range(len(self)//2 - 1, -1, -1):
            self.float_down(i)

    def float_up(self, index):
        """如果index位置的元素>父节点元素，那么上浮
        """
        while index > 0:
            parent = (index - 1) // 2
            if self._array[index] > self._array[parent]:
                self.swap(index, parent)
                index = parent
            else:
                break

    def float_down(self, index):
        """使堆中小的数沉下去，保证堆的一条根节点->叶子节点的路有序。
        """
        while index < len(self._array) // 2:  # index还处在父节点范围
            left_child, right_child = 2 * i + 1, 2 * i + 2
            # 左右孩子较大的节点
            max_index = left_child  # 初始化为左节点,因为左节点一定存在
            if right_child < len(self) and self._array[left_child] < self._array[right_child]:
                # 如果右节点存在且右节点小
                max_index = right_child
            if self._array[index] < self._array[max_index]:
                self.swap(index, max_index)
            index = max_index

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
