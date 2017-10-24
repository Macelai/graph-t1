class Graph:
    
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
        if v1 not in self.__verticies or v2 not in self.vertices:
            raise VertexNotFoundException(\
                    "At least one vertex doesn't belongs to the graph.")
        self.__vertices[v1].discard(v2)
