#! usr/bin/env python
# -*-coding:utf-8-*-

"""
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增的。
"""


class LinkedList(object):

    def __init__(self, value=None, p_next=None):
        self.value = value
        self.p_next = p_next

    def __repr__(self):
        return "节点值为 %d" % self.value


def merge_list(p_head_one, p_head_two):
    """
    :param p_head_one 链表1头指针
    :param p_head_two 链表2头指针
    :function 合并链表
    """
    if not p_head_one:
        return p_head_two
    elif not p_head_two:
        return p_head_one
    else:
        p_new_head = LinkedList()
        if p_head_one.value >= p_head_two.value:
            """如果链表1的节点值大"""
            p_new_head = p_head_two
            p_head_two = p_head_two.p_next
            p_new_head.p_next = merge_list(p_head_one, p_head_two)
        else:
            """如果链表2的节点值大或者链表1已经遍历完"""
            p_new_head = p_head_one
            p_head_one = p_head_one.p_next
            p_new_head.p_next = merge_list(p_head_one, p_head_two)
        return p_new_head


if __name__ == '__main__':
    node4 = LinkedList(5)
    node3 = LinkedList(3, node4)
    node2 = LinkedList(2, node3)
    node7 = LinkedList(7)
    node6 = LinkedList(5, node7)
    node5 = LinkedList(3, node6)
    p_new_head = merge_list(node2, node5)
    while p_new_head:
        print(p_new_head)
        p_new_head = p_new_head.p_next
