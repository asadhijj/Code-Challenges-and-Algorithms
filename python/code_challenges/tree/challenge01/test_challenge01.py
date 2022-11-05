import pytest
from challenge01 import *

def test_build_tree():
    tree = TreeBuilder()
    assert tree.buildTree([3,9,20,15,7],[9,3,15,20,7]).val == 3
    assert tree.buildTree([3,9,20,15,7],[9,3,15,20,7]).left.val == 9
    assert tree.buildTree([3,9,20,15,7],[9,3,15,20,7]).right.val == 20
    assert tree.buildTree([3,9,20,15,7],[9,3,15,20,7]).right.left.val == 15
    assert tree.buildTree([3,9,20,15,7],[9,3,15,20,7]).right.right.val == 7

def test_build_tree2():
    tree = TreeBuilder()
    assert tree.buildTree([-1],[-1]).val == -1

def test_build_tree3():
    tree = TreeBuilder()
    assert tree.buildTree([1,2,3],[2,1,3]).val == 1
    assert tree.buildTree([1,2,3],[2,1,3]).left.val == 2
    assert tree.buildTree([1,2,3],[2,1,3]).right.val == 3