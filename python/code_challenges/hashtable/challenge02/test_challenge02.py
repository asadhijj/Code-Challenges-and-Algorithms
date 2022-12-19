from challenge02 import repeated_word
import pytest

def test_repeated_word_one():
    expected = "ASAC"
    actual = repeated_word("ASAC is a department at LTUC. ASAC teaches programming in LTUC.")
    assert actual == expected

def test_repeated_word_two():
    expected = "No Repetition"
    actual = repeated_word("I am learning programming at ASAC.")
    assert actual == expected

def test_repeated_word_three():
    expected = "Python"
    actual = repeated_word("Python is the best language in programming. I am learning Python at ASAC")
    assert actual == expected
