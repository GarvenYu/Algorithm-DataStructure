#! usr/bin/env python
# -*-coding:UTF-8 -*-

"""
实现一个函数按照之字形顺序打印二叉树,即第一行按照从左到右,第二层按照从右到左,第三层再按照从左到右,以此类推。
"""


class BinaryTreeNode(object):

    def __init__(self, data=None, left=None, right=None):
        self.value = data
        self.left_node = left
        self.right_node = right

    def __repr__(self):
        return str(self.value) + '\nleft:' + \
            str(self.left_node.value) + '\nright:' + str(self.right_node.value)


def buildBinaryTree(preOrder, inOrder):
    """前序序列和中序序列构造二叉树"""
    if not inOrder or not preOrder:
        return None
    else:
        root = BinaryTreeNode()
        root.value = preOrder[0]
        root.left_node = buildBinaryTree(preOrder[1:inOrder.index(
            preOrder[0])+1], inOrder[:inOrder.index(preOrder[0])])
        root.right_node = buildBinaryTree(preOrder[inOrder.index(
            preOrder[0])+1:], inOrder[inOrder.index(preOrder[0])+1:])
        return root


class ArrayStack(object):

    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, item):
        if item:
            self.size += 1
            self.stack.append(item)
        pass

    def pop(self):
        if self.size:
            self.size -= 1
            return self.stack.pop()
        return None


def print_tree_by_letter(root_node, stack_odd, stack_even):
    """
    按照之字形打印二叉树;
    奇数层先放左节点再放右节点,偶数层先放右节点再放左节点;
    :param stack_odd 存储奇数层node栈
    :param stack_even 存储偶数层node栈
    """
    if not root_node or not stack_odd or not stack_even:
        return None
    else:
        level = 1
        stack_odd.push(root_node)
        while stack_odd.size or stack_even.size:
            if level & 0x01:
                # 奇数
                while stack_odd.size:
                    p_node = stack_odd.pop()
                    print(p_node.value, end="")
                    if p_node.left_node:
                       stack_even.push(p_node.left_node)
                    if p_node.right_node:
                       stack_even.push(p_node.right_node)
                print("\n", end="")
                level += 1
            else:
                # 偶数
                while stack_even.size:
                    p_node = stack_even.pop()
                    print(p_node.value, end="")
                    if p_node.right_node:
                       stack_odd.push(p_node.right_node)
                    if p_node.left_node:
                       stack_odd.push(p_node.left_node)
                print("\n", end="")
                level += 1


if __name__ == '__main__':
    preOrder = [1, 2, 4, 8, 9, 5, 10, 11, 3, 6, 12, 13, 7, 14, 15]
    inOrder = [8, 4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15]
    stack_odd = ArrayStack()
    stack_even = ArrayStack()
    if preOrder or inOrder:
        root = buildBinaryTree(preOrder, inOrder)
        print_tree_by_letter(root, stack_odd, stack_even)
    else:
        print('Invalid Data')
