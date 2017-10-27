#!/usr/bin/env python

import unittest
from graph import Graph, VertexNotFoundException

class GraphTest(unittest.TestCase):

    def test_is_on_graph(self):
        g = Graph()
        g.add_vertex('a')
        self.assertTrue('a' in g.vertices())


    def test_not_on_graph(self):
        g = Graph()
        self.assertFalse(bool(g.vertices()))


if __name__ == "__main__":
    unittest.main()
