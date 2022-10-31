import pytest
from challenge02 import *

def test_Validation():
    s=Solution()
    actual =s.parenthese_Validation('()')
    expected = True
    assert actual == expected

def test_Validation1():
    s=Solution()
    actual = s.parenthese_Validation('(){}[]')
    expected = True
    assert actual == expected

def test_Validation3():
    s=Solution()
    actual = s.parenthese_Validation('(]')
    expected = False
    assert actual == expected

def test_Validation4():
    s=Solution()
    actual = s.parenthese_Validation('"[(hello)()]"')
    expected = True
    assert actual == expected

def test_Validation5():
    s=Solution()
    actual = s.parenthese_Validation('{[Hello]}')
    expected = True
    assert actual == expected

def test_Validation6():
    s=Solution()
    actual = s.parenthese_Validation('{[Hello]')
    expected = False
    assert actual == expected