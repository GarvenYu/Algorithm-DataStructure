#! usr/bin/env python
#-*-coding:utf-8-*-

"""
实现一个函数，判断一棵二叉树是否是对称的，如果一棵二叉树和它的镜像一样，那么它是对称的。
思路：比较二叉树的前序遍历序列(root->left->right)和对称遍历序列(root->right->left)
"""


def is_tree_symmetric(node):
    """判断是否是对称树"""
    if not node:
        return True
    else:
        return is_tree_symmetric_core(node._left, node._right)


def is_tree_symmetric_core(node1, node2):
    if node1 == node2 == None:
        return True
    if not node1 or not node2:
        return False
    if node1._data != node2._data:
        return False
    return is_tree_symmetric_core(node1._left, node2._right) \
        and is_tree_symmetric_core(node1._right, node2._left)
