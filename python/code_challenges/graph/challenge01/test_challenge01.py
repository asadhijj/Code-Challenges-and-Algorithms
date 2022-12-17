import pytest
from challenge01 import Graph

def test_breadth_first_one():
    g = Graph()
    node_a = g.add_node("a")
    node_b = g.add_node("b")
    node_c = g.add_node("c")
    node_d = g.add_node("d")
    node_e = g.add_node("e")
    node_f = g.add_node("f")
    node_g = g.add_node("g")
    g.add_edge(node_a, node_b)
    g.add_edge(node_a, node_c)
    g.add_edge(node_b, node_c)
    g.add_edge(node_c, node_d)
    g.add_edge(node_c, node_e)
    g.add_edge(node_d, node_f)
    g.add_edge(node_e, node_f)
    g.add_edge(node_f, node_g)
    actual = g.breadth_first(node_c)
    expected = ["c", "a", "b", "d", "e", "f", "g"]
    assert actual == expected

def test_breadth_two():
    g = Graph()
    node_a = g.add_node("a")
    node_b = g.add_node("b")
    node_c = g.add_node("c")
    node_d = g.add_node("d")
    node_e = g.add_node("e")
    node_f = g.add_node("f")
    node_g = g.add_node("g")
    g.add_edge(node_a, node_b)
    g.add_edge(node_a, node_c)
    g.add_edge(node_b, node_c)
    g.add_edge(node_c, node_d)
    g.add_edge(node_c, node_e)
    g.add_edge(node_d, node_f)
    g.add_edge(node_e, node_f)
    g.add_edge(node_f, node_g)
    actual = g.breadth_first(node_g)
    expected = ["g", "f", "d", "e", "c", "a", "b"]
    assert actual == expected