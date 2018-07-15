#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
python实现链表依赖于类生成的实例，每个节点都是一个对象，组合在一起形成一个完整链表
Node类：data 和 _pNext 
LinkedList：head,默认是node; __length,列表的长度

链表的一些常用操作：
append(value):在链表末添加node/值 
insert(value, index):插入 
delete(index):删除 
getValueByIndex(index):查找 
clear():清空链表 
printLinkedList():打印整个链表
'''


class Node(object):
    def __init__(self, data):
        '''
        初始化Node
        '''
        self._data = data
        self._pNext = None

    def __repr__(self):
        return str(self._data)


class LinkedList(object):
    def __init__(self):
        '''
        LinkedList初始化
        '''
        self.__length = 0
        self._pHead = None

    def append(self, newNode):
        '''
        向链表末尾添加Node
        '''
        if isinstance(newNode, Node):
            pass
        else:
            newNode = Node(newNode)
        if self.__length == 0:
            self._pHead = newNode
        else:
            node = self._pHead
            while node._pNext:
                node = node._pNext
            node._pNext = newNode
        self.__length += 1

    def insert(self, newNode, index):
        '''
        指定位置插入一个节点
        '''
        if type(index) is int:
            if index > self.__length:
                print('index out of range')
                return
            else:
                if isinstance(newNode, Node):
                    pass
                else:
                    newNode = Node(newNode)
                currentNode = self._pHead  # 当前节点
                prevNode = None  # 前一个节点
                currentIndex = 1  # 起始位置
                if index == currentIndex:
                    newNode._pNext = self._pHead
                    self._pHead = newNode
                else:
                    while currentIndex <= self.__length:
                        currentIndex += 1
                        prevNode = currentNode
                        currentNode = currentNode._pNext
                        if index == currentIndex:
                            '''
                            a->b====> a->newNode->b
                            '''
                            prevNode._pNext = newNode
                            newNode._pNext = currentNode
                self.__length += 1
                return
        else:
            print('index is not int')
            return

    def delete(self, index):
        '''
        指定位置删除节点
        '''
        if type(index) is int:
            if index > self.__length:
                print('index out of range')
                return
            else:
                currentNode = self._pHead
                prevNode = None
                if index == 1:
                    self._pHead = currentNode._pNext
                else:
                    while index - 1:
                        prevNode = currentNode
                        currentNode = currentNode._pNext
                        index -= 1
                    '''
                    index=0
                    '''
                    prevNode._pNext = currentNode._pNext
                self.__length -= 1
                return
        else:
            print('index is not int')
            return

    def getValueByIndex(self, index):
        '''
        获取指定位置的值
        '''
        if type(index) is int:
            if index > self.__length:
                print('index out of range')
                return
            else:
                currentNode = self._pHead
                while index-1:
                    currentNode = currentNode._pNext
                    index -= 1
                print('index=%d,data=%d' % (index, currentNode._data))
                return
        else:
            print('index is not int')
            return

    def clear(self):
        '''
        清空链表
        '''
        self._pHead = None
        self.__length = 0


def printLinkedListReverse(currentNode):
    '''
    从后向前打印整个链表
    后进先出结构可用栈实现,递归本质上是结构,所以可用递归
    '''
    if currentNode:
        if currentNode._pNext:
            printLinkedListReverse(currentNode._pNext) # 压栈
        print(str(currentNode._data)+'->', end='') # 出栈逻辑


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    linkedList = LinkedList()
    linkedList.append(node1)
    linkedList.append(node2)
    linkedList.append(node3)
    printLinkedListReverse(linkedList._pHead)
