#! usr/bin/env python
# -*-coding:utf-8-*-

"""
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后的链表头节点。
"""


class LinkedList(object):

    def __init__(self, value=None, p_next=None):
        self.value = value
        self.p_next = p_next

    def __repr__(self):
        return "节点值为 %d" % self.value


def reverse_linked_list(p_head):
    """反转链表"""
    if not p_head:
        return None
    if not p_head.p_next:
        return p_head
    p_prev = None
    p_curr = p_head
    p_behind = p_curr.p_next
    while p_behind:
        # 进行反转,并移动三个指针
        p_curr.p_next = p_prev
        p_prev = p_curr
        p_curr = p_behind
        p_behind = p_curr.p_next
    p_curr.p_next = p_prev
    return p_curr


if __name__ == '__main__':
    node4 = LinkedList(4)
    node3 = LinkedList(3, node4)
    node2 = LinkedList(2, node3)
    print(reverse_linked_list(node2))
