import pytest
from challenge03 import *


@pytest.fixture
def tree_maker_one():
    tree_one=Tree()
    array= [0,-3,-10,5,9]
    root=tree_one.listToBts(array)
    return tree_one.making_the_tree(root)

@pytest.fixture
def tree_maker_two():
    tree_two=Tree()
    array=  [1,3]
    root=tree_two.listToBts(array)
    return tree_two.making_the_tree(root)

@pytest.fixture 
def tree_empty_test():
    tree_empty=Tree()
    array=[]
    root=tree_empty.listToBts(array)
    return tree_empty.making_the_tree(root)

def test_listToBts_one(tree_maker_one):
    actual = tree_maker_one
    expected = [0, -3, 9, -10, 5]
    assert actual == expected
    


def test_listToBts_two(tree_maker_two):
    actual = tree_maker_two
    expected = [3, 1]
    assert actual == expected


def test_edge(tree_empty_test):
    actual =tree_empty_test
    expected ="Tree is empty"
    assert actual == expected
