class Stack:
    def __init__ (self):
        self.data = []
    def push (self, x):
        self.data.append(x)
    def pop (self):
        if self.is_empty():
            print "The Stack is empty"
        else:
            return self.data.pop()
    def display (self):
        return self.data
    def is_empty (self):
        return self.data == []

class Queue:
    def __init__ (self):
        self.data = []
    def enqueue (self, x):
        self.data.append(x)
    def dequeue (self):
        if self.is_empty():
            print "The Stack is empty"
        else:
            return self.data.pop(0)
    def display (self):
        return self.data
    def is_empty (self):
        return self.data == []

# Implement a MyQueue class which implements a queue using two stacks
class MyQueue:
    def __init__ (self):
        self.s1 = Stack()
        self.s2 = Stack()
    def dequeue (self):
        if self.s2.is_empty():
            while self.s1.is_empty()==False:
                self.s2.push(self.s1.pop())
        if self.s2.is_empty():
            print "The MyQueue is empty"
        else:
            return self.s2.pop()
    def enqueue (self, x):
        self.s1.push(x)
    def count (self):
        print "There are %s elements in MyQueue"%(len(self.s1.data)+len(self.s2.data))
    def is_empty (self):
        return len(self.s1.data)+len(self.s2.data) == 0

