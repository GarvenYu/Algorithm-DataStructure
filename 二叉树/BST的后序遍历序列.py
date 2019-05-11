#! usr/bin/env python
# -*-coding:utf-8-*-

"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历序列，是则返回True，否则返回False，
假设输入的数组任意两个数字都不相同。
思路：
1.二叉搜索树左子树<根节点<右子树
2.后序遍历序列：左节点、右节点、根节点
"""


def is_bst_post_order(seq):
    if not seq:
        return False
    return is_bst_post_order_core(seq)


def is_bst_post_order_core(seq):
    if not seq:
        return
    length = len(seq)
    root = seq[-1]
    i = 0
    while seq[i] < root:
        i += 1
    j = i
    while j < length - 1:
        if seq[j] < root:
            return False
        j += 1
    # 左子树
    is_bst_post_order_core(seq[:i])
    # 右子树
    is_bst_post_order_core(seq[i:-1])
    return True


if __name__ == '__main__':
    post_order = [1, 2, 3, 4, 5]  # 没有右子树的BST
    # [1,2,3,4,5].reverse()  # 没有左子树的BST
    # post_order = [5, 7, 6, 9, 11, 10, 8] # 正常情况
    # post_order = [1] # 单节点
    if is_bst_post_order(post_order):
        print("是后序遍历序列")
    else:
        print("不是后序遍历序列")
