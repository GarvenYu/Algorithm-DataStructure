#! usr/bin/env python
#-*-coding:utf-8-*-

"""
定义栈的数据结构,请在该类型中实现一个能够得到栈的最小元素的min函数。在该栈中，调用min、push、pop的
时间复杂度都是O(1)。
"""

class ArrayStack(AbstractStack):
	"""
	Stack的列表实现
	主栈:3214(bot->top)
	辅助栈:3211(bot->top)
	"""
	AUX_STACK = ArrayStack() # 辅助栈保存每次push操作后主栈的最小元素

	def push(self, item):
		"""MIN_DATA保存当前最小的元素,"""
		self.push(item)
		if self.AUX_STACK.is_empty() or self.AUX_STACK.top_item()<item:
			"""如果辅助栈为空或者辅助栈最上面的元素小于item"""
			self.AUX_STACK.push(item) 
		else:
			self.AUX_STACK.push(self.AUX_STACK.top_item()) # 否则将上一步的最小元素再入栈一次代表执行到此步它还是最小元素

	def pop(self):
		if not self.isEmpty():
			return self.pop()
		return None

	def top_item(self):
		return self.pop()

	@classmethod
	def pop_min_item(cls):
		"""输出栈内最小元素"""
		return cls.AUX_STACK.top_item()