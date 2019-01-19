#! usr/bin/env python
# -*-coding:utf-8-*-

"""
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后的链表头节点。
"""

from typing import Optional


class LinkedList(object):

    def __init__(self, value=None, p_next=None):
        self.value = value
        self.p_next = p_next

    def __repr__(self):
        return "节点值为 %d" % self.value


def reverse_linked_list(p_head: LinkedList) -> Optional[LinkedList]:
    """反转链表"""
    p_prev = None
    p_curr = p_head
    while p_curr:
        p_prev, p_prev.p_next, p_curr = p_curr, p_prev, p_curr.p_next
    return p_prev


def print_all(head: LinkedList):
    nums = []
    current = head
    while current:
        nums.append(current.value)
        current = current.p_next
    print("->".join(str(num) for num in nums))


if __name__ == '__main__':
    node4 = LinkedList(4)
    node3 = LinkedList(3, node4)
    node2 = LinkedList(2, node3)
    print_all(reverse_linked_list(node2))
