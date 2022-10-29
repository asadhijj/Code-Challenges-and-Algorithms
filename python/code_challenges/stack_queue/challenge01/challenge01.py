class Node:
    '''Class to define and make a node'''
    def __init__(self,value):
        self.next = None
        self.value = value

class Stack:
    '''Class for stacks functions and its attributes'''
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self,value):
        '''pushes a new node to the top of the stack'''
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        '''removes the node from the top of the stack, and returns the node’s value'''
        if self.top:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            return temp.value
        else:
            return("This stack is empty")
    
    def peek(self):
        '''returns the value of the node located on top of the stack, without removing it from the stack'''
        if self.top:
            return self.top.value
        else:
            return("This stack is empty")

    def empty(self):
        '''returns a boolean indicating whether or not the stack is empty'''
        return self.size == 0

    def get_size(self):
        '''Returns the size of the stack'''
        return self.size



class myQueue:
    def __init__(self):
        """Initialize your data structure here."""
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x: int) -> None:
        """Push element x to the back of queue."""
        while not self.stack2.empty():
          self.stack1.push(self.stack2.pop())
        self.stack1.push(x)
        
    def pop(self) -> int:
        """Removes the element from in front of queue and returns that element."""
        self.peek()
        return self.stack2.pop()

    def pop2(self) -> int:
        """Removes the element from in front of queue and returns that element."""
        while not self.stack1.empty():
          self.stack2.push(self.stack1.pop())
        return self.stack2.pop()
        
    def peek(self) -> int:
        """Get the front element."""
        while not self.stack1.empty():
          self.stack2.push(self.stack1.pop())
        return self.stack2.peek()
        
    def empty(self) -> bool:
        """Returns whether the queue is empty."""
        return self.stack1.empty() and self.stack2.empty()


my_queue = myQueue()  
my_queue.push(1)
my_queue.push(2)
print(my_queue.pop())
print(my_queue.peek())
print(my_queue.empty())