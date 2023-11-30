import igraph as ig
import pytest

def test_add_vertices_positive():
    n = 3
    g = ig.Graph()
    g.add_vertices(n)
    assert n == g.vcount()

def test_add_vertices_zero():
    n = 0
    g = ig.Graph()
    g.add_vertices(0)
    assert n == g.vcount()

def test_add_edges_one_pair():
    g = ig.Graph(5,directed=True)
    edge = (1,2)
    g.add_edges([edge])
    assert edge in g.get_edgelist()
def test_add_many_edges():
    g = ig.Graph(6,directed=True)
    edges = [(1,2),(4,3),(0,1),(3,3)]
    g.add_edges(edges)
    for edge in edges:
        assert edge in g.get_edgelist()

def test_to_tuple_list_many():
    n_vertices = 5
    edges = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (3, 4)]
    g = ig.Graph(n_vertices,edges,directed=True)
    l = g.to_tuple_list()
    for edge in edges:
        assert edge in l

def test_to_tuple_list_empty():
    g = ig.Graph()
    assert g.to_tuple_list() == []

def test_union_empty():
    g1 = ig.Graph()
    g2 = ig.Graph()
    assert g1.union(g2).get_edgelist() == []

def test_union_non_empty():
    n_vertices1 = 5
    edges1 = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (3, 4)]
    g1 = ig.Graph(n_vertices1, edges1, directed=True)
    n_vertices2 = 6
    edges2 = [(1, 2), (4, 3), (0, 1), (3, 3),(5,5)]
    g2 = ig.Graph(n_vertices2,edges2,directed=True)
    assert sorted(g1.union(g2).get_edgelist()) == sorted(set(edges1+edges2))

def test_is_acyclic_in_cyclic():
    n_vertices = 4
    edges = [(0,1),(1,2),(2,3),(3,1)]
    g = ig.Graph(n_vertices,edges,directed=True)
    assert g.is_acyclic() == False

def test_is_acyclic_in_acyclic():
    n_vertices = 4
    edges = [(0,1),(3,1),(1,2)]
    g = ig.Graph(n_vertices,edges,directed=True)
    assert g.is_acyclic() == True
