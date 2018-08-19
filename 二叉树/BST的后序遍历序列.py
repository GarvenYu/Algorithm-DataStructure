#! usr/bin/env python
#-*-coding:utf-8-*-

"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历序列，是则返回True，否则返回False，
假设输入的数组任意两个数字都不相同。
思路：
1.二叉搜索树左子树<根节点<右子树
2.后序遍历序列：左节点、右节点、根节点
"""


def is_bst_post_order(post_order):
    """
    判断输入序列是否是BST的后序遍历序列
    :param post_order 后序遍历序列
    """
    if not post_order:
        return False
    else:
        return is_bst_post_order_core(post_order, len(post_order))


def is_bst_post_order_core(post_order, length):
    root = post_order[-1]  # 取根节点
    small = 0  # 左子树指针
    for i in range(0, length - 1):
        if post_order[i] >= root:
            break
        small += 1
    large = small  # 右子树指针起始位置
    for j in range(large, length - 1):
        if post_order[j] < root:
            return False
    left_sub = True
    if small > 0:
        # 判断左子树
        left_sub = is_bst_post_order_core(post_order[:small], small)
    right_sub = True
    if large < length - 1:
        # 判断右子树
        right_sub = is_bst_post_order_core(
            post_order[large:length], length - small - 1)
    return left_sub and right_sub


if __name__ == '__main__':
    post_order = [1, 2, 3, 4, 5]  # 没有右子树的BST
    # post_order = [1,2,3,4,5].reverse()  # 没有左子树的BST
    # post_order = [5, 7, 6, 9, 11, 10, 8] # 正常情况
    # post_order = [1] # 单节点
    if is_bst_post_order(post_order):
        print("是后序遍历序列")
    else:
        print("不是后序遍历序列")
