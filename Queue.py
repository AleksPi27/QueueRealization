from Node import Node


class Queue:

    def __init__(self):
        self.length = 0
        self.head = None

    def isEmpty(self):
        return self.length == 0

    def push(self, node):
        obj = Node(node)
        obj.next = None
        if self.head is None:
            self.head = obj
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = obj
        self.length += 1

    def top(self):
        if self.length == 0:
            print("The queue is empty")
            return None
        return self.head.data

    def pop(self):
        if (self.length == 0):
            print("The queue is empty")
            return None

        firstElement = self.head
        self.head = firstElement.next
        self.length -= 1
        return firstElement.data

    def size(self):
        return self.length
