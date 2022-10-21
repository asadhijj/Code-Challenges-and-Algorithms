class Node:
     def __init__(self, x):
         self.val = x
         self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, node):
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
    
    def deleteNode(self, node):
 
        if not node:
            return
        
        node.val = node.next.val
        node.next = node.next.next
    
    def printAll(self):
        elements=[]
        if self.head is None:
            print("The linked list is empty")
        else:
            current = self.head
            while current is not None:
                elements.append(current.val)
                current = current.next
            return elements
                


llist = LinkedList()
node1 = Node(4)
llist.append(node1)

node2 = Node(9)
llist.append(node2)

node3 = Node(5)
llist.append(node3)

node4 = Node(1)
llist.append(node4)

print(llist.printAll())

llist.deleteNode(node3)
print(llist.printAll())

