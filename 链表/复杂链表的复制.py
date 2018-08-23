#! usr/bin/env python
#-*-coding:utf-8-*-

"""
实现一个函数,复制一个复杂链表。在复杂链表中，每个节点除了有一个指向下一节点的指针，
还有一个指针指向链表中的任意节点或者None。
"""


class ComplexListNode(object):

    def __init__(self, value, p_next=None, p_sibling=None):
        self.value = value
        self.p_next = p_next
        self.p_sibling = p_sibling

    def traverse(self):
        """遍历链表"""
        while self:
            if self.p_sibling:
                print("value-%d,sibling-%d" %
                      (self.value, self.p_sibling.value))
            else:
                print("value-%d,no sibling" % (self.value))
            self = self.p_next

# 思路1


def clone_with_dict(p_head):
    """
    时间复杂度O(n)
    空间复杂度O(n)
    dict存储<N,N'>,O(1)时间内可找到N'的p_sibling	
    """
    if not p_head:
        return None
    else:
        p_node = p_head
        p_clone_head = ComplexListNode(p_node.value)
        p_clone = p_clone_head
        d = dict()  # 记录原始节点和复制节点的映射
        d[p_node] = p_clone
        while p_node.p_next:
            # 复制原始链表上的每个节点,并用p_next连接起来
            p_clone_next = ComplexListNode(p_node.p_next.value)
            p_clone.p_next = p_clone_next
            p_clone = p_clone.p_next
            p_node = p_node.p_next
            d[p_node] = p_clone
        p_node = p_head
        while p_node:
            # 设置p_sibling
            if p_node.p_sibling:
                d[p_node].p_sibling = d[p_node.p_sibling]
            p_node = p_node.p_next
        return p_clone_head

# 思路2


def clone_nodes(p_head):
    """根据原始节点N创建N',并链接到N后面形成A-A'-B-B'"""
    p_node = p_head
    while p_node:
        p_clone = ComplexListNode(p_node.value)
        p_clone.p_next = p_node.p_next
        p_node.p_next = p_clone
        p_node = p_clone.p_next


def connect_sibling_nodes(p_head):
    """
    设置N'的p_sibling
    如果A的p_sibling是C,那么A'的p_sibling是C'(C.p_next)
    """
    p_node = p_head
    while p_node:
        p_clone = p_node.p_next
        if p_node.p_sibling:
            p_clone.p_sibling = p_node.p_sibling.p_next
        p_node = p_clone.p_next


def reconnect_nodes(p_head):
    """
    重新链接N'各个节点形成复制链表
    奇数位置的节点链接起来是原始链表;偶数位置的节点链接起来是复制链表
    """
    p_node = p_head
    p_clone_head = p_clone = p_node.p_next
    p_node.p_next = p_clone.p_next
    p_node = p_node.p_next
    while p_node:
        p_clone.p_next = p_node.p_next
        p_clone = p_clone.p_next
        p_node.p_next = p_clone.p_next
        p_node = p_node.p_next
    return p_clone_head


def clone(p_head):
    """
    时间复杂度O(n)
    不使用辅助空间
    """
    if not p_head:
        return None
    else:
        # 根据原始节点N创建N',并链接到N后面形成A-A'-B-B'
        clone_nodes(p_head)
        # 设置N'的p_sibling
        connect_sibling_nodes(p_head)
        # 重新链接N'各个节点形成复制链表
        return reconnect_nodes(p_head)

if __name__ == '__main__':
    node3 = ComplexListNode(3)
    node2 = ComplexListNode(2, p_next=node3)
    node1 = ComplexListNode(1, p_next=node2, p_sibling=node3)  # 1-2-3
    clone_node1 = clone_with_dict(node1)
    clone_node2 = clone(node1)
    clone_node1.traverse()
    clone_node2.traverse()
