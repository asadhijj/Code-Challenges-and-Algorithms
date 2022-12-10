import pytest
from challenge01 import Solution, Tree


def test_sum_true():
    tree1 = Tree(7)
    tree1.left = Tree(2)
    tree1.left.left = Tree(1)
    tree1.left.right = Tree(5)
    tree1.right = Tree(9)
    tree1.right.right = Tree(14)
    test=Solution()
    actual = test.findTarget(tree1,3)
    expected = True
    assert actual == expected

def test_sum_false():
    tree1 = Tree(7)
    tree1.left = Tree(2)
    tree1.left.left = Tree(1)
    tree1.left.right = Tree(5)
    tree1.right = Tree(9)
    tree1.right.right = Tree(14)
    test2=Solution()
    actual = test2.findTarget(tree1, 4)
    expected = False
    assert actual == expected



def test_sum_empty():
    tree1 = Tree()
    test3=Solution()
    actual = test3.findTarget(tree1, 4)
    expected = False
    assert actual == expected