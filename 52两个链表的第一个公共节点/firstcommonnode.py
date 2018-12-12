#! usr/bin/env python3
# -*-coding:utf-8-*-

"""
输入两个链表，找出它们的第一个公共节点。
1.蛮力法，复杂度O(n^2)；
2.使用两个辅助栈s1和s2，分别存储两个链表的节点，每次都出栈一个元素，直到最后一个相同元素即为第一个公共节点。
时间复杂度O(n) 空间复杂度O(n)；
3.遍历得到两个链表的长度l1和l2，l1先前进l1-l2步，然后一起遍历直到找到第一个公共节点；
"""


class LinkedList(object):

    def __init__(self, data, linkedlist):
        self._data = data
        self._next = linkedlist


def find_first_common_node(l1: LinkedList, l2: LinkedList):
    if not l1 or not l2:
        return None
    len1 = len2 = 0
    current_node1 = head_node1 = l1
    current_node2 = head_node2 = l2
    while current_node1:
        len1 += 1
        current_node1 = current_node1._next
    while current_node2:
        len2 += 1
        current_node2 = current_node2._next
    if len1 != len2:
        if len1 > len2:
            for steps in range(0, len1 - len2):
                head_node1 = head_node1._next
        else:
            for steps in range(0, len2 - len1):
                head_node2 = head_node2._next
    while head_node1._next:
        if head_node1._next == head_node2._next:
            return head_node1._next._data
        else:
            head_node1 = head_node1._next
            head_node2 = head_node2._next
    return None  # 没有公共节点


node4 = LinkedList(4, None)
node3 = LinkedList(3, node4)
node2 = LinkedList(2, node3)
node1 = LinkedList(1, node2)
node5 = LinkedList(5, node3)
print(find_first_common_node(node1, node5))  # 3