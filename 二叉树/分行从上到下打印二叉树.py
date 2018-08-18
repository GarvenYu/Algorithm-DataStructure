#! usr/bin/env python
#-*-coding:utf-8-*-

"""
从上到下按层打印二叉树,同一层的节点按从左到右的顺序打印，每一层打印到一行。
"""


class ArrayQueue(object):

    def __init__(self):
        self.queue = []
        self.size = 0

    def push_back(self, item):
        if item:
            self.size += 1
            self.queue.insert(0, item)
        pass

    def pop_front(self):
        if self.size:
            self.size -= 1
            return self.queue.pop()
        return None


class BinaryTreeNode(object):

    def __init__(self, data=None, left=None, right=None):
        self.value = data
        self.left_node = left
        self.right_node = right

    def __repr__(self):
        return str(self.value) + '\nleft:' + \
            str(self.left_node.value) + '\nright:' + str(self.right_node.value)


def buildBinaryTree(preOrder, inOrder):
    """前序序列和中序序列构造二叉树"""
    if not inOrder or not preOrder:
        return None
    else:
        root = BinaryTreeNode()
        root.value = preOrder[0]
        root.left_node = buildBinaryTree(preOrder[1:inOrder.index(
            preOrder[0])+1], inOrder[:inOrder.index(preOrder[0])])
        root.right_node = buildBinaryTree(preOrder[inOrder.index(
            preOrder[0])+1:], inOrder[inOrder.index(preOrder[0])+1:])
        return root


def print_tree_by_row(root_node, queue):
    """分行打印二叉树"""
    if not root_node or not queue:
        pass
    else:
        queue.push_back(root_node)
        to_be_printed = 1  # 将要被打印的节点数
        next_level_printed = 0  # 下一层要被打印的节点数
        while queue.size:
            p_node = queue.pop_front()
            print(p_node.value, end="")
            if p_node.left_node:
                queue.push_back(p_node.left_node)
                next_level_printed += 1
            if p_node.right_node:
                queue.push_back(p_node.right_node)
                next_level_printed += 1
            to_be_printed -= 1
            if not to_be_printed:
                # 打印完一层
                print("\n", end="")
                to_be_printed = next_level_printed
                next_level_printed = 0


if __name__ == '__main__':
    preOrder = [8, 6, 5, 7, 10, 9, 11]
    inOrder = [5, 6, 7, 8, 9, 10, 11]
    queue = ArrayQueue()
    # preOrder = [1,2,3]
    # inOrder = [2,1,3]
    if preOrder or inOrder:
        root = buildBinaryTree(preOrder, inOrder)
        print_tree_by_row(root, queue)
    else:
        print('Invalid Data')
