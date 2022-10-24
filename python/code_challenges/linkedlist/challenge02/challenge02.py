class Node:
    '''This is a class to define nodes'''
    def __init__(self, x):
         self.val = x
         self.next = None

class LinkedList:
    '''This is class to create linked list methods'''
    def __init__(self):
        self.head = None

    def append(self, node):
        '''This method is made to accept nodes and append them to the the linked list'''
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
    
    
    def middleNode(self):
        '''this is a method to find the middle node and takes in consideration the even numbers of nodes and odd numbers
        it iterates through the list using two pointers, one pointer to run to the end value,
        and the other pointer to catch the middle node when the first node reaches the end value'''
        pointer = self.head
        mid_node = self.head
        while ( pointer ) :
            if pointer.next != None :
                pointer = pointer.next.next
                mid_node = mid_node.next
            else : break
        return mid_node.val 
    
    def printAll(self):
        '''this is a method to print the linked list values inside of a list'''
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
    '''This function is made to delete nodes accessing only the node and takes in consideration
    that the node is not a tail node'''
 
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