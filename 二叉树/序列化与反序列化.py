#! usr/bin/env python
#-*-coding:utf-8-*-

"""
实现两个函数,分别用来序列化和反序列化二叉树。
"""
global head_index
head_index = 0

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


def serialize(head_node):
    node = head_node
    if not node:
        print("$,", end="")
        return
    print("%d," % node.value, end="")  # 根节点
    serialize(node.left_node)  # 左子树
    serialize(node.right_node)  # 右子树


def deserialize(serialize_list, length):
    global head_index
    if head_index < length:
        if serialize_list[head_index] != '$':
            node = BinaryTreeNode(data=serialize_list[head_index])
            head_index += 1
            print("%d" % head_index)
            node.left_node = deserialize(serialize_list, length)
            head_index += 1
            print("%d" % head_index)
            node.right_node = deserialize(serialize_list, length)
            return node
        else:
            return None
    else:
        return


if __name__ == '__main__':
    preOrder = [1, 2, 4, 3, 5, 6]
    inOrder = [4, 2, 1, 5, 3, 6]
    # preOrder = [1,2,3]
    # inOrder = [2,1,3]
    if preOrder or inOrder:
        root = buildBinaryTree(preOrder, inOrder)
        serialize(root)
        print("")
        serialize_list = [1, 2, 4, '$', '$', '$', 3, 5, '$', '$', 6, '$', '$']
        head_node = deserialize(serialize_list, len(serialize_list))
        serialize(head_node)
    else:
        print('Invalid Data')
