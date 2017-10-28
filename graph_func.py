from graph import Graph

def isregular(g):
    x = g.arbitrary_vertex()
    d = g.degree(x)
    for v in g.vertices():
        if g.degree(v) != d:
            return False
    return True


def iscomplete(g):
    ...


def transitive_closure(g):
    ...


def isconnected(g):
    ...


def istree(g):
    ...
