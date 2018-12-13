# !usr/bin/env python3
# -*-coding:utf-8-*-

"""
题目：输入一棵二叉树的根节点，判断它是否是平衡二叉树。
示例：如果某二叉树任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
"""


class TreeNode(object):

    def __init__(self, data, left=None, right=None):
        self._data = data
        self._left = left
        self._right = right


def is_balance_tree_1(root):
    """非平衡树的本质是在某一个节点,它的左(右)子树为空,而右(左)子树不为空,且它还有至少一个孩子节点"""
    if not root:
        return True
    else:
        if not root._left:  # 如果左子树空
            if root._right and (root._right._left or root._right._right):  # 右子树不空且有孩子节点
                return False  # 非平衡树
            else:
                is_balance_tree_1(root._right)
        if not root._right:  # 如果右子树空
            if root._left and (root._left._left or root._left._right):  # 左子树不空且有孩子节点
                return False  # 非平衡树
            else:
                is_balance_tree_1(root._left)
        return is_balance_tree_1(root._left) and is_balance_tree_1(root._right)


def is_balance_tree_2(root):
    """进行后序遍历并记录每个节点的深度值,这样也不会有重复遍历"""
    if not root:
        return True, 0
    result1, left_depth = is_balance_tree_2(root._left)
    result2, right_depth = is_balance_tree_2(root._right)
    if -1 <= left_depth - right_depth <= 1:
        return True, max(left_depth, right_depth) + 1
    else:
        return False, max(left_depth, right_depth) + 1


node5 = TreeNode(5)
node4 = TreeNode(4, None, node5)
node3 = TreeNode(3, None, node4)
node2 = TreeNode(2)
node1 = TreeNode(1, node2, node3)
print(is_balance_tree_1(node1))  # False
print(is_balance_tree_2(node1))  # (False, 4)
