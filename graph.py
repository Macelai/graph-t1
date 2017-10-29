
"""
It represents a Graph, providing the following basic operations and informations:
    vertex addition;
    vertex remotion;
    edge addition (connection between two vertices);
    edge remotion;
    order of graph (number of vertices);
    the vertices set;
    a any vertex;
    adjacent vertices to a vertex;
    degree of a vertex.
"""
class Graph(object):
    
    def __init__(self, v, obj = None):
        self.__vertices = dict()
        self.add_vertex(v, obj)


    def add_vertex(self, v, obj = None):
        if v not in self.__vertices:
            self.__vertices[v] = [obj, set()]


    def remove_vertex(self, v):
        if v not in self.__vertices:
            raise VertexNotFoundException

        for vertex in self.__vertices:
            self.__vertices[vertex].discard(v)

        del self.__vertices[v]


    def get_ref(self, v):
        return self.__vertices[v][0]


    def add_edge(self, v1, v2):
        if v1 not in self.__vertices or v2 not in self.__vertices:
            raise VertexNotFoundException(\
                    "At least one vertex doesn't belongs to the graph.") 
        self.__vertices[v1][1].add(v2)


    def remove_edge(self, v1, v2):
        if v1 not in self.__vertices or v2 not in self.__vertices:
            raise VertexNotFoundException(\
                    "At least one vertex doesn't belongs to the graph.")
        self.__vertices[v1].discard(v2)


    def order(self):
        return len(self.__vertices)


    def vertices(self):
        return set(self.__vertices.keys())


    def arbitrary_vertex(self):
        return self.vertices().pop()


    def adjacent(self, v):
        if v not in self.__vertices:
            raise VertexNotFoundException("Vertex not found.")
        return self.__vertices[v][1]

    
    def degree(self, v):
        return len(self.adjacent(v))


    def as_dict(self):
        return self.__vertices


    def transitive_closure(self, v, closure):
        for v in self.adjacent(v):
            if v not in closure:
                closure.add(v)
                self.transitive_closure(v, closure)
        return closure



class VertexNotFoundException(Exception):

    def __init__(self, message = ''):
        self.message = message


    def __str__(self):
        repr(self.message)
