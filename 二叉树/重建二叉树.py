#!usr/bin/env python
# -*- coding: UTF-8 -*-

"""
输入二叉树的前序遍历和中序遍历的结果，重建二叉树并输出头节点，假设中序遍历和前序遍历的结果中都不含重复数字。
"""


class BinaryTreeNode(object):

    def __init__(self, data=None, left=None, right=None):
        self.value = data
        self.left_node = left
        self.right_node = right

    def __repr__(self):
        return str(self.value) + '\nleft:' + \
            str(self.left_node.value) + '\nright:' + str(self.right_node.value)


def buildBinaryTree(preOrder, inOrder):
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


def postOrder(root):
    if not root.value:
        return []
    else:
       return postOrder(root.left_node) + postOrder(root.right_node) + [root.value]


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
