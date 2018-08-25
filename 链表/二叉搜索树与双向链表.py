#! usr/bin/env python
#-*-coding:utf-8-*-

"""
输入一棵二叉搜索树,将该二叉搜索树转换成一个排序的双向链表。
不能创建新的节点,只能调整树中节点指针的指向。
"""


def convert_bst_to_list(head_node):
    if not head_node:
        return None
    else:
        last_node = None  # 指向双向链表的尾节点
        convert_bst_to_list_core(head_node, last_node)
        new_head_node = last_node
        while new_head_node.left_node:
            new_head_node = new_head_node.left_node
        return new_head_node


def convert_bst_to_list_core(head_node, last_node):
    """中序遍历"""
    if not head_node:
        return
    cur_node = head_node
    if cur_node.left_node:
        convert_bst_to_list_core(cur_node.left_node, last_node) # 左子树
    # 根节点
    # last_node 可保存上一步遍历过的节点,进而方便设置右节点   
    cur_node.left_node = last_node
    if last_node:
        last_node.right_node = cur_node
    last_node = cur_node
    if cur_node.right_node:
        convert_bst_to_list_core(cur_node.right_node, last_node) # 右子树
