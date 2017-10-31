"""
It represents a Graph, providing the following basic operations:
    vertex addition;
    vertex remotion;
    edge addition (connection between two vertices);
    edge remotion;
    order of graph (number of vertices);
    the vertices set;
    a any vertex;
    adjacent vertices to a vertex;
    degree of a vertex;
    topological sorting;
    transitive closure of an vertex.
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
            self.__vertices[vertex][1].discard(v)

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

    
    def exit_degree(self, v):
        return len(self.adjacent(v))


    def entry_degree(self, v):
        deg = 0
        for x in self.__vertices:
            if v in self.__vertices[x][1]:
                deg += 1
        return deg
    

    def degree(self, v):
        return self.exit_degree(v) + self.entry_degree(v)

    
    def fonts(self):
        fonts = set()
        for v in self.__vertices:
            if self.entry_degree(v) == 0:
                fonts.add(v)
        return fonts


    def as_dict(self):
        return self.__vertices


    def transitive_closure(self, v, closure):
        for v in self.adjacent(v):
            if v not in closure:
                closure.add(v)
                self.transitive_closure(v, closure)
        return closure

    
    def get_topological_sorting(self):
        import graph_func as funcs
        v = self.arbitrary_vertex()
        if funcs.hascycle(self, v, v, set()):
            raise DoesNotApplyException("Graph isn't a DAG")

        top_sort = []
        visited = set()
        for f in self.fonts():
            self.topological_sorting(f, visited, top_sort)

        return list(reversed(top_sort))


    def topological_sorting(self, v, visited, top_sort):        
        visited.add(v)
        for x in self.adjacent(v):
            if x not in visited:
                self.topological_sorting(x, visited, top_sort)
        top_sort.append(v)



### Exception classes ###

class VertexNotFoundException(Exception):

    def __init__(self, message = ''):
        self.message = message


    def __str__(self):
        repr(self.message)



class DoesNotApplyException(Exception):

    def __init__(self, message = ''):
        self.message = message


    def __str__(self):
        repr(self.message)
