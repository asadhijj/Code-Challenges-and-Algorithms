import pytest
from challenge01 import *

def test_push():
    '''testing the push fucntion'''
    my_queue = myQueue()
    my_queue.push(1)
    my_queue.push(2)
    my_queue.push(3)
    my_queue.push(4)
    expected = 1
    actual = my_queue.peek()
    assert actual == expected

def test_pop():
    '''testing the pop function'''
    my_queue = myQueue()
    my_queue.push(1)
    my_queue.push(2)
    my_queue.push(3)
    my_queue.push(4)
    expected = 1
    actual = my_queue.pop()
    assert actual == expected


def test_empty_False():
    '''testing the empty function when the queue is not empty'''
    my_queue = myQueue()

    my_queue.push(1)
    my_queue.push(2)
    my_queue.push(3)
    my_queue.push(4)
    expected = False
    actual = my_queue.empty()
    assert actual == expected

def test_empty_True():
    '''Testing the empty function when the queue is empty'''
    my_queue = myQueue()

    my_queue.push(1)
    my_queue.push(2)
    my_queue.pop()
    my_queue.pop()
    expected = True
    actual = my_queue.empty()
    assert actual == expected