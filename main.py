#!/usr/bin/env python

from graph import Graph, VertexNotFoundException


if __name__ == "__main__":
    g = Graph()
    
    # test remove vertex that isn't in graph
    try:
        g.remove_vertex('vertex')
        print('TEST FAILED: removing vertex! Line 10')
    except:
        print("Error removing vertex v1. Test OK")


    # test adding edge
    g.add_vertex('v1')
    g.add_vertex('v2')
    try:
        g.add_edge('v1', 'v2')
        print("Edge (v1, v2) added! Test OK")
    except:
        print("TEST FAILED: adding edge! Line 20")
   

   # test removing edge
    try:
        g.remove_edge('v1', 'v2')
        print("Edge (v1, v2) removed! Test OK")
    except:
        print("TEST FAILED: removing edge! line 28")


    # test adding edge with vertex that isn't in graph
    try:
        g.add_edge('v1', 'v3')
        print("TEST FAILED: adding edge! line 36")
    except:
        print("Error adding edge (v1, v3)! Test OK")

