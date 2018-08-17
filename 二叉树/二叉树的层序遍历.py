#! usr/bin/env python
# -*-coding:utf-8-*-

"""
从上到下，同一层从左到右的顺序打印二叉树的每个节点。
"""

class ArrayQueue(object):
	"""ArrayQueue的实现"""
	def __init__(self, arg):
		pass

	def pop_front(self):
		"""头元素出队列"""
		pass

	def push_back(self):
		"""尾元素入队列"""
		pass

def print_node(root_node):
	"""输出node的值"""
	if not root_node.value:
		return None
	else:
		print(root_node.value)

def tree_level_traversal(queue, root_node):
	if not queue or not root_node:
		return None
	else:
		# 根节点入队列
		# 打印节点值
		# 节点左右子树入队列
		queue.push_back(root_node)
		while queue.size():
			p_node = queue.pop_front()
			print_node(p_node)
			if p_node.left_node:
				queue.push_back(p_node.left_node)
			if p_node.right_node:
				queue.push_back(p_node.right_node)