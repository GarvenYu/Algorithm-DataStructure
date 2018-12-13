# !usr/bin/env python3
# -*-coding:utf-8-*-

"""
题目：输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点(含根、叶节点)形成树的一条路径，
最长路径的长度为树的深度。根节点深度为1。
"""


class TreeNode(object):

    def __init__(self, data, left=None, right=None):
        self._data = data
        self._left = left
        self._right = right


def get_tree_depth(root):
    if not root:
        return 0
    else:
        left_depth = get_tree_depth(root._left)
        right_depth = get_tree_depth(root._right)
        return max(left_depth, right_depth) + 1
