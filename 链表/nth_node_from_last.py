#! usr/bin/env python
# -*-coding:utf-8-*-

"""
输入一个链表，输出该链表中倒数第K个节点。(从1开始计数)
"""


def find_last_k_node(p_head, k):
    """找到倒数第K个节点"""
    if not p_head or k <= 0 or not isinstance(k, int):
        return None
    p_ahead = p_head
    while k - 1:
        if p_ahead.p_next:
            p_ahead = p_ahead.p_next
            k -= 1
        else:
            # K > 节点总数
            return None
    p_behind = p_head
    while p_ahead.p_next:
        p_ahead = p_ahead.p_next
        p_behind = p_behind.p_next
    return p_behind
