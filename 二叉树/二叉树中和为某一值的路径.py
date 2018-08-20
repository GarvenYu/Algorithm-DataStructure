#! usr/bin/env python
#-*-coding:utf-8-*-

"""
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从根节点开始往下一直到叶节点所经过的节点形成一条路径。
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

    STACK_CAPACITY = 10

    def __init__(self):
        self.stack = [None] * self.STACK_CAPACITY
        self.size = 0

    def push(self, item):
        """未实现栈动态扩容"""
        self.stack[self.size] = item
        self.size += 1

    def pop(self):
        """未实现栈动态缩减"""
        if not self.is_empty():
            pop_item = self.stack[self.size - 1]
            del self.stack[self.size - 1]
            self.size -= 1
            return pop_item
        return None

    def top_item(self):
        """取栈顶元素"""
        if not self.is_empty():
            pop_item = self.stack[self.size - 1]
            return pop_item
        return None

    def is_empty(self):
        """判断栈是否为空"""
        return self.size == 0

    def traverse(self):
        """遍历栈 bot->top"""
        if self.size:
            for i in range(0, self.size):
                print("%d " % self.stack[i].value, end="")
            print("") # 换行
        else:
            print("None", end="")


def print_path(root, condition):
    """
    打印路径
    :param root 二叉树根节点
    :param condition 输入的整数
    """
    if not root or not isinstance(condition, int):
        print("Invalid Data")
    else:
        stack = ArrayStack()
        print_path_core(root, condition, stack)


def print_path_core(root, condition, stack, path_sum=0):
    stack.push(root)
    path_sum += root.value
    if root.left_node:
        # 左子树不为空
        print_path_core(root.left_node, condition, stack, path_sum)
    if root.right_node:
        # 右子树不为空
        print_path_core(root.right_node, condition, stack, path_sum)
    if not root.left_node and not root.right_node:
        # 叶子节点
        # 比较condition与path_sum
        if condition == path_sum:
            # 打印路径
            stack.traverse()
    # 回退到父节点
    path_sum -= root.value
    stack.pop()            


if __name__ == '__main__':
    preOrder = [1, 2, 4, 5, 6]
    inOrder = [4, 2, 5, 1, 6]
    if preOrder or inOrder:
        root = buildBinaryTree(preOrder, inOrder)
        print_path(root, 7)
    else:
        print('Invalid Data')