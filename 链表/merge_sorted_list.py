#! usr/bin/env python
# -*-coding:utf-8-*-

"""
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增的。
"""
from typing import Optional


class LinkedList(object):

    def __init__(self, value=None, p_next=None):
        self.value = value
        self.p_next = p_next

    def __repr__(self):
        return "节点值为 %d" % self.value


def merge_list(p_head_one: LinkedList, p_head_two: LinkedList) -> Optional[LinkedList]:
    """
    :param p_head_one 链表1头指针
    :param p_head_two 链表2头指针
    :function 合并链表
    """
    if p_head_one and p_head_two:
        p1, p2 = p_head_one, p_head_two
        fake_node = LinkedList()  # 哨兵
        current = fake_node
        while p1 and p2:
            if p1.value <= p2.value:
                current.p_next = p1
                p1 = p1.p_next
            else:
                current.p_next = p2
                p2 = p2.p_next
            current = current.p_next
        current.p_next = p1 if p1 else p2
        return fake_node.p_next
    return p_head_one or p_head_two


def print_all(head: LinkedList):
    nums = []
    current = head
    while current:
        nums.append(current.value)
        current = current.p_next
    print("->".join(str(num) for num in nums))
