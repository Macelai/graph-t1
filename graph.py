class Graph:
    
    def __init__(self):
        self.__vertices = dict()

    def add_vertex(self, v):
        if v not in self.__vertices:
            self.__vertices[v] = set()

    def remove_vertex(self, v):
        if v in self.__veritices:
            for vertex in self.__vertifices:
                self.__vertices[vertex].discard(v)
            del self.__vertices[v]
        else:
            print("Vertex not found")

    def add_edge(self, v1, v2):
        if v1 in self.__vertices and v2 in self.__vertices:
            self.__vertices[v1].add(v2)
            self.__vertices[v2].add(v1)
        else:
            print("One or two vertices not found")

    def remove_edge(self, v1, v2):
        if v1 in self.__verticies and v2 in self.vertices:
            self.__vertices[v1].discard(v2)
            self.__vertices[v2].discard(v1)
        else:
            print("One or two vertices not found")
