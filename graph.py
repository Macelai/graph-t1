"""
It represents a Graph with the following basic operations:
    vertex addition;
    vertex remotion;
    edge addition (connection between two vertices);
    edge remotion;
    order of graph (number of vertices);
    to provide the vertex set;
    to provide a specific vertex;
    to provide adjacent vertices;
    degree of an vertex.

And the additional functions:

"""
class Graph(object):
    
    def __init__(self):
        self.__vertices = dict()


    def add_vertex(self, v):
        if v not in self.__vertices:
            self.__vertices[v] = set()


    def remove_vertex(self, v):
        if v not in self.__vertices:
            raise VertexNotFoundException

        for vertex in self.__vertices:
            self.__vertices[vertex].discard(v)
        del self.__vertices[v]


    def add_edge(self, v1, v2):
        if v1 not in self.__vertices or v2 not in self.__vertices:
            raise VertexNotFoundException(\
                    "At least one vertex doesn't belongs to the graph.") 
        self.__vertices[v1].add(v2)


    def remove_edge(self, v1, v2):
        if v1 not in self.__vertices or v2 not in self.__vertices:
            raise VertexNotFoundException(\
                    "At least one vertex doesn't belongs to the graph.")
        self.__vertices[v1].discard(v2)


    def single_vertex(self, v):  # tentar um nome melhor
        if v not in self.__vertices:
            raise VertexNotFoundException("Vertex not found.")
        return self.__vertices[v]


    def order(self):
        return len(self.__vertices)


    def vertices(self):
        return set(self.__vertices.keys())


    def vertex(self, something):
        ...  # ?


    def adjacent(self, v):
        if v not in self.__vertices:
            raise VertexNotFoundException("Vertex not found.")
        return self.--vertices[v]

    
    def degree(self, v):
        return len(self.adjacent(v))


class VertexNotFoundException(Exception):

    def __init__(self, message = ''):
        self.message = message


    def __str__(self):
        repr(self.message)
