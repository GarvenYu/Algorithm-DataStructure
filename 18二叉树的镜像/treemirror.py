#!usr/bin/env python
# -*- coding: UTF-8 -*-

"""
输入一棵二叉树，输出它的镜像。
"""


class TreeNode(object):

    def __init__(self, data=None, left=None, right=None):
        self._data = data
        self._left = left
        self._right = right

    def __str__(self):
        if not self._left and not self._right:
            return '[%d]' % self._data
        else:
            return '(%d,%s,%s)' % (self._data, self._left, self._right)


def tree_mirror_recursion(node):
    """递归"""
    if not node:
        return
    node._left, node._right = node._right, node._left
    tree_mirror_recursion(node._left)
    tree_mirror_recursion(node._right)


def tree_mirror_loop(root):
    """非递归"""
    if not root:
        return
    # 保存当前需要交换的节点集合
    parent_array = [root]
    while parent_array:
        # 保存下一次循环需要交换的节点
        child_array = []
        for node in parent_array:
            node._left, node._right = node._right, node._left
            if node._left:
                child_array.append(node._left)
            if node._right:
                child_array.append(node._right)
        parent_array = child_array


if __name__ == '__main__':
    left_node = TreeNode(data=2)
    right_node = TreeNode(data=3)
    root = TreeNode(data=1, left=left_node, right=right_node)
    tree_mirror_recursion(root)
    print(str(root))
    tree_mirror_loop(root)
    print(str(root))
