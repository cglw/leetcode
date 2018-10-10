# -*- coding: utf-8 -*-
# @Time : 2018/10/10 上午10:46
# @Author : chengang
# @File : 09_array_queue.py
# @Function:

# class Node:
#     def __init__(self, data, next=None):
#         self._next = next
#         self.data = data
#
# class LinkQueue:
#
#     def __init__(self):


class ArrayQueue:

    def __init__(self, n):
        self.n = n
        self.items = []
        print (len(self.items))
        self.head = 0
        self.tail = 0

    def get_items(self):
        return self.items

    # 入队
    def enqueue(self, item):
        if self.tail == self.n:
            return False
        self.items.append(item)
        self.tail += 1
        return True

    # 出队
    def dequeue(self):
        if self.head == self.tail:
            return None
        res = self.items.pop(0)
        self.head += 1
        return res


z = ArrayQueue(5)
z.enqueue(6)
z.enqueue(9)
z.enqueue(5)
z.enqueue(9)
z.enqueue(10)
print (z.enqueue(12))
print (z.dequeue())
