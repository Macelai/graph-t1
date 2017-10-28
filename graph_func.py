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


def transitive_closure(g, v, closure):
    for v in g.adjacent(v):
        print("for ", v)
        if v not in closure:
            closure.add(v)
            transitive_closure(g, v, closure)
    return closure


def isconnected(g):
    ...


def istree(g):
    ...
