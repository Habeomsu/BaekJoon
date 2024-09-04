class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None

    def push(self,data):
        if self.top is None:
            self.top=Node(data)
        else:
            node=Node(data)
            node.next=self.top
            self.top=node

    def pop(self):
        if self.top is None:
            return None
        else:
            node=self.top
            self.top=self.top.next
            return node.data

    def peek(self):
        if self.top is None:
            return None
        return  self.top.data

    def is_empty(self):
        if self.top is None:
            return True
