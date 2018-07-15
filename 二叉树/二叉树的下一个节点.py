#! usr/bin/env python
# -*-coding:UTF-8 -*-
"""
给定一棵二叉树和其中的一个节点，找出中序遍历序列的下一个节点。树中的节点除了指向左右子节点，还有指向父节点。
1.如果该节点有右子树，则下一节点是右子树的最左子节点；
2.如果该节点没有右子树，且该节点是父节点的左子节点，下一节点是父节点；
3.如果该节点没有右子树，且该节点是父节点的右子节点，向上找到某个节点，该节点是它父节点的左子节点，下一节点是该节点的父节点。
"""
class TreeNode(object):
	def __init__(self):
		self.left = None
		self.right = None
		self.parent = None

def findNext(node):
	if node.right:
		# 最左子节点
		childNode = node.right
		while childNode.left:
			childNode = childNode.left
		return childNode
	elif not node.right and (node == node.parent.left):
		return node.parent
	elif not node.right and (node == node.parent.right):
		# 向上找到某个节点，该节点是它父节点的左子节点，下一节点是该节点的父节点
		parentNode = node.parent
		while parentNode == parentNode.parent.right:
			parentNode = parentNode.parent
		return parentNode.parent

if __name__ == '__main__':
	node = TreeNode()
	nextNode = findNext(node)