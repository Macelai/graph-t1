from graph import Graph

def isregular(g):
    x = g.arbitrary_vertex()
    d = g.degree(x)
    for v in g.vertices():
        if g.degree(v) != d:
            return False
    return True


def iscomplete(g):
    degree = g.order() - 1
    for v in g.vertices():
        if g.degree(v) != degree:
            return False
    return True


def isconnected(g):
    x = g.arbitrary_vertex()
    return g.vertices() == g.transitive_closure(x, set())
    

def istree(g):
    v = g.arbitrary_vertex()
    return isconnected(g) and not hascicle(g, v, v, set())


def hascycle(g, v, prev, visited):
    if v in visited:
        return True

    visited.add(v)
    for vertex in g.adjacent(v):
        if vertex != prev and hascycle(g, vertex, v, visited):
            return True

    visited.remove(v)
    return False
