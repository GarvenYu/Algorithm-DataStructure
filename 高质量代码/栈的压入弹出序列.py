#! usr/bin/env python
#-*-coding:utf-8-*-

"""
输入两个整数序列，第一个序列表示栈的压入顺序，判断第二个序列是否为栈的弹出顺序。
假设入栈的所有数字均不相等。
"""


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


def is_pop_order(array_stack, push_order, pop_order, push_size, pop_size):
    """
    判断是否为弹出顺序
    :param array_stack
    :param push_order
    :param pop_order
    :param push_size
    :param pop_size
    """
    if not push_order or not pop_order or not array_stack:
        return None
    if push_size != pop_size:
        return None
    push_index = 0  # 入栈序列指针
    for i in range(0, pop_size):
        if array_stack.top_item() == pop_order[i]:
            # 栈顶元素与出栈序列元素相等
            array_stack.pop()
            continue
        elif push_index < push_size:
            # 入栈序列还没遍历结束
            for j in range(push_index, push_size):
                if push_order[j] != pop_order[i]:
                    # 入栈
                    push_index += 1
                    array_stack.push(push_order[j])
                    if push_index == push_size:
                        # push_order中不含pop_order元素
                        return False
                else:
                    push_index += 1
                    break

        else:
            # 栈顶元素不等于出栈序列元素而且入栈序列已遍历完
            return False
    return True

if __name__ == '__main__':
    push_order = [1, 2, 3, 4, 5]
    pop_order = [3, 5, 4, 2, 1]
    array_stack = ArrayStack()
    print(is_pop_order(array_stack, push_order, pop_order, 5, 5))
