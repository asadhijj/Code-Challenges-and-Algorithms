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
    
    
    def middleNode(self):
        pointer = self.head
        mid_node = self.head
        while ( pointer ) :
            if pointer.next != None :
                pointer = pointer.next.next
                mid_node = mid_node.next
            else : break
        return mid_node.val 
    
    def printAll(self):
        elements=[]
        if self.head is None:
            return("The linked list is empty")
        else:
            current = self.head
            while current is not None:
                elements.append(current.val)
                current = current.next
            return elements
                

def deleteNode(node):
 
    if not node:
        return
        
    node.val = node.next.val
    node.next = node.next.next
        
        
        
llist = LinkedList()
node1 = Node(4)
llist.append(node1)

node2 = Node(9)
llist.append(node2)

node3 = Node(5)
llist.append(node3)

node4 = Node(1)
llist.append(node4)

node5 =Node(7)
llist.append(node5)
node6 = Node(3)
llist.append(node6)

deleteNode(node3)
print(llist.printAll())

print(llist.middleNode())