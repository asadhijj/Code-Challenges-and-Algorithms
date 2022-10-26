import pytest
from challenge03 import *


def test_removenth_node_1():
    '''A test to see if the remove nth node method is working for n =3'''
    llist = LinkedList()
    node1 = Node(4)
    node2 = Node(9)
    node3 = Node(5)
    node4 = Node(1)
    node5 = Node(7)
    node6 = Node(3)
    llist.append(node1)
    llist.append(node2)
    llist.append(node3)
    llist.append(node4)
    llist.append(node5)
    llist.append(node6)
    llist.removenthNode(llist.head,3)
    expected = [4,9,5,7,3]
    actual = llist.printAll()
    assert actual == expected

def test_removenth_node_2():
    '''A test to see if the remove nth node method is working for n =2'''
    llist = LinkedList()
    node1 = Node(4)
    node2 = Node(9)
    node3 = Node(5)
    node4 = Node(1)
    node5 = Node(7)
    node6 = Node(3)
    llist.append(node1)
    llist.append(node2)
    llist.append(node3)
    llist.append(node4)
    llist.append(node5)
    llist.append(node6)
    llist.removenthNode(llist.head,2)
    expected = [4,9,5,1,3]
    actual = llist.printAll()
    assert actual == expected  
def test_empty():
    '''a test to see if the error message works in case there is no nodes in the linked list'''
    llist = LinkedList()

    expected = "The linked list is empty"
    actual = llist.printAll()

    assert actual ==expected