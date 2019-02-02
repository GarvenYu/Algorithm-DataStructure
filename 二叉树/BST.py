#! usr/bin/env python3
# -*-coding:utf-8-*-
import random


class BST(object):
    def __init__(self, value, left=None, right=None):
        self._value = value
        self._left = left
        self._right = right

    def add_node(self, value: int):
        """插入节点"""
        root = self
        while True:
            if value < root._value:
                if not root._left:
                    root._left = BST(value)
                    break
                else:
                    root = root._left
            else:
                if not root._right:
                    root._right = BST(value)
                    break
                else:
                    root = root._right

    @staticmethod
    def in_order(node):
        """中序遍历"""
        if not node:
            return []
        return node.in_order(node._left) + [node._value] + node.in_order(node._right)

    def delete(self, value: int):
        """删除节点"""
        node = self
        parent = None
        while node and node._value != value:
            parent = node
            node = node._left if value < node._value else node._right
        if not node:
            return False
        if node._left and node._right:
            # two childs
            # 删除节点替换为右子树的最左子节点
            child = node._right
            pre_parent = node
            while child._left:
                pre_parent = child
                child = child._left
            # 删除node
            node._value = child._value
            # 记录删除位置的上下文
            parent, node = pre_parent, child
        # one child or no child
        child = node._left if node._left else node._right
        if not parent:
            self._value = None if not child else child._value
            self._left = self._right = None
        elif parent._left == node:
            parent._left = child
        else:
            parent._right = child
        return True

    def find(self, value: int):
        """查找"""
        node = self
        while node and node._value != value:
            if value < node._value:
                node = node._left
            else:
                node = node._right
        if node:
            return True
        return False
