#!/usr/bin/env python

from graph import Graph, VertexNotFoundException
from curriculum import Curriculum

if __name__ == "__main__":
    g = Graph()
    
    c = Curriculum()

    c.populate_graph()
