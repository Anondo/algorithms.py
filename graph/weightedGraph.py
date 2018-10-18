class Node(object):
    def __init__(self , name = "" , distance = None):
        self.name = name
        self.distance = distance
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.__str__()

class Edge(object):
    def __init__(self , nodes , weight = 0):
        self.nodes = tuple(nodes)
        self.weight = weight
    def __str__(self):
        return str(self.nodes)
    def __repr__(self):
        return self.__str__()

class Graph(object):
    def __init__(self , graph = None):
        if not graph:
            graph = {}
        self.graph = graph
        self.nodes = []
        self.edges = []

    def add_vertex(self , data):
        self.graph[data] = []
        self.nodes.append(data)



    def add_edge(self , nodes , weight = 0):
        nodes = tuple(nodes)
        vrtx1 , vrtx2 = nodes
        edge = Edge(nodes , weight)
        if vrtx1 in self.nodes and vrtx2 in self.nodes:
            self.graph[vrtx1].append(vrtx2)
            self.graph[vrtx2].append(vrtx1)
            self.edges.append(edge)

    def getVertices(self):
        return self.nodes

    def getEdges(self , node = None):
        if(not node):
            return self.edges
        else:
            return filter(lambda edge : node in edge.nodes    , self.edges)


#graph_elements = { "a" : ["b","c"],
#                "b" : ["a", "d"],
#                "c" : ["a", "d"],
#                "d" : ["e"],
#                "e" : ["d"]
#                }

'''
graph = Graph()
vertex1 = Node("a")
vertex2 = Node("b")
vertex3 = Node("c")
vertex4 = Node("d")
vertex5 = Node("e")


graph.add_vertex(vertex1)
graph.add_vertex(vertex2)
graph.add_vertex(vertex3)
graph.add_vertex(vertex4)
graph.add_vertex(vertex5)

graph.add_edge((vertex1, vertex2) , 12)
graph.add_edge((vertex1, vertex3) , 3)
graph.add_edge((vertex2, vertex4) , 5)
graph.add_edge((vertex3, vertex4) , 7)
graph.add_edge((vertex4, vertex5) , 9)

print graph.getEdges()
print graph.getVertices()
print graph.graph
'''
