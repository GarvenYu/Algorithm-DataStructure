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

    def __repr__(self):
        return str(self._data) + '\nleft:' + \
            str(self._left._data) + '\nright:' + str(self._right._data)


def tree_mirror(node):
    if not node:
        return None
    else:
        tree_mirror_core(node)


def tree_mirror_core(node):
    if not node:
        return
    node._left, node._right = node._right, node._left
    tree_mirror_core(node._left)
    tree_mirror_core(node._right)


def in_order_traverse(node):
    """中序遍历"""
    if not node:
        return []
    else:
        return in_order_traverse(node._left)+[node._data]+in_order_traverse(node._right)

if __name__ == '__main__':
    left_node = TreeNode(data=2)
    right_node = TreeNode(data=3)
    node = TreeNode(data=1, left=left_node, right=right_node)
    tree_mirror(node)
    print(in_order_traverse(node))