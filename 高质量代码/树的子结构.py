#!usr/bin/env python
# -*- coding: UTF-8 -*-

"""
输入两棵二叉树A和B,判断B是不是A的子结构。
思路1：输出两棵树的中序遍历序列,看B是否是A的子序列。
思路2：在A中找到B的根节点;判断此根节点的子树与B是否相等
"""


class TreeNode(object):

    def __init__(self, data=None, left=None, right=None):
        self._data = data
        self._left = left
        self._right = right

    def __repr__(self):
        return str(self._data) + '\nleft:' + \
            str(self._left._data) + '\nright:' + str(self._right._data)


def in_order_traverse(node):
    """中序遍历"""
    if not node:
        return []
    else:
        return in_order_traverse(node._left)+[node._data]+in_order_traverse(node._right)


def have_root_b(node_a, node_b):
    """判断A中是否有B的根节点"""
    if not node_a or not node_b:
        return False
    else:
        result = (node_a._data == node_b._data)
        if result:
            result = have_subtree(node_a, node_b)
        if not result:
            result = have_root_b(node_a._left, node_b)
        if not result:
            result = have_root_b(node_a._right, node_b)
        return result


def have_subtree(node_a, node_b):
    """判断A中是否有B的子树"""
    if not node_b:
        return True
    if not node_a:
        # node_b非空而node_a为空
        return False
    if node_a._data != node_b._data:
        # 都不为空
        return False
    return have_subtree(node_a._left, node_b._left) \
        and have_subtree(node_a._right, node_b._right)


if __name__ == '__main__':
    left_node = TreeNode(data=2)
    right_node = TreeNode(data=3)
    node = TreeNode(data=1, left=left_node, right=right_node)
    node_b = TreeNode(data=1, left=left_node, right=None)
    print(have_root_b(node, node_b))