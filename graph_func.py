from graph import Graph

def isregular(g):
    x = g.arbitrary_vertex()
    d = g.exit_degree(x) + g.entry_degree(x)
    for v in g.vertices():
        v_deg = g.exit_degree(v) + g.entry_degree(v)
        if v_deg != d:
            return False
    return True


def iscomplete(g):
    degree = g.order() - 1
    for v in g.vertices():
        deg_v = g.exit_degree(v) + g.entry_degree(v)
        if deg_v != degree:
            return False
    return True


def isconnected(g):
        return g.vertices() == g.transitive_closure(g.arbitrary_vertex(), set())
    

def istree(g):
    v = g.arbitrary_vertex()
    return isconnected(g) and not hascicle(g, v, v, set())


def hascycle(g, v, prev, visited):
    if v in visited:
        return True

    visited.add(v)
    for vertex in g.adjacent(v):
        if vertex != prev:
            if hascycle(g, vertex, v, visited):
                return True

    visited.remove(v)
    return False
