# usr/bin/emv python
# -*-coding:utf-8-*-

# Description:Given a singly linked list, determine if it is a palindrome.
# Follow up:
# Could you do it in O(n) time and O(1) space?

# 思路：快指针每次走2步，慢指针每次走1步。当快指针走到结尾，慢指针走到了中间，慢指针边走边改变前半部分
# 链表使其逆序，比较左右两部分是否相同。


class ListNone(object):
    """定义链表节点
    """

    def __init__(self, data: int, next=None):
        self._data = data
        self._next = next


def reverse(node, targetnode):
    """反转链表
    :param targetnode 中间节点
    """
    prev = None
    while node and node != targetnode:
        _next = node._next
        node._next = prev
        prev = node
        node = _next
    return prev


def ispalindrome(node) -> bool:
    """判断是否是回文
    :param node 单链表头结点
    :return bool
    """
    if not node:
        return False
    fastnode = node
    slownode = node
    # 找到中间节点
    while fastnode and fastnode._next:
        slownode = slownode._next
        fastnode = fastnode._next._next
    # slownode为中间节点
    newheadnode = reverse(node, slownode)
    # 比较左右两个链表
    while newheadnode._next and slownode._next:
        if newheadnode._data == slownode._data:
            newheadnode = newheadnode._next
            slownode = slownode._next
        else:
            return False
    return True


node4 = ListNone('a')
node3 = ListNone('b', next=node4)
node2 = ListNone('b', next=node3)
node1 = ListNone('a', next=node2)
if ispalindrome(node1):
    print('Yes')
else:
    print('No')
