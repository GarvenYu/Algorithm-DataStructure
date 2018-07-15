#!usr/bin/env python
# -*- coding: UTF-8 -*-

"""
输入二叉树的前序遍历和中序遍历的结果，重建二叉树并输出头节点，假设中序遍历和前序遍历的结果中都不含重复数字。
"""


class BinaryTreeNode(object):

    def __init__(self, data=None):
        self._data = data
        self._left = None
        self._right = None

    def __repr__(self):
        return str(self._data) + '\nleft:' + \
            str(self._left._data) + '\nright:' + str(self._right._data)


def buildBinaryTree(preOrder, inOrder):
    root = BinaryTreeNode()  # 根节点
    if len(inOrder) < 1:
        return root
    elif len(inOrder) >= 1:
        root._data = preOrder[0]
        root._left = buildBinaryTree(preOrder[1:inOrder.index(
            preOrder[0])+1], inOrder[:inOrder.index(preOrder[0])])
        root._right = buildBinaryTree(preOrder[inOrder.index(
            preOrder[0])+1:], inOrder[inOrder.index(preOrder[0])+1:])
        return root


def postOrder(root):
    if not root._data:
        return []
    else:
       return postOrder(root._left) + postOrder(root._right) + [root._data]


if __name__ == '__main__':
    preOrder = [1, 2, 4, 7, 3, 5, 6, 8]
    inOrder = [4, 7, 2, 1, 5, 3, 8, 6]
    # preOrder = [1,2,3]
    # inOrder = [2,1,3]
    if preOrder or inOrder:
        root = buildBinaryTree(preOrder, inOrder)
        print(postOrder(root))
    else:
        print('Invalid Data')
