import pytest
from challenge02 import *


def test_middle_node_even():
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

    expected = 1
    actual = llist.middleNode()
    assert actual == expected

def test_middle_node_odd():
    llist = LinkedList()
    node1 = Node(4)
    node2 = Node(9)
    node3 = Node(5)
    node5 = Node(7)
    node6 = Node(3)
    llist.append(node1)
    llist.append(node2)
    llist.append(node3)
    llist.append(node5)
    llist.append(node6)

    expected = 5
    actual = llist.middleNode()
    assert actual == expected

    
def test_empty():
    llist = LinkedList()

    expected = "The linked list is empty"
    actual = llist.printAll()

    assert actual ==expected