class Graph(object):
    def __init__(self , graph = None):
        if not graph:
            graph = {}
        self.graph = graph

    def add_vertex(self , data):
        self.graph[data] = []


    def add_edge(self , edge):
        (vrtx1 , vrtx2) = tuple(edge)
        if vrtx1 in self.graph.keys() and vrtx2 in self.graph.keys():
            self.graph[vrtx1].append(vrtx2)
            self.graph[vrtx2].append(vrtx1)

    def getVertices(self):
        return self.graph.keys()

    def getEdges(self):
        edgename = []
        for vrtx in self.graph.keys():
            for nxtvrtx in self.graph[vrtx]:
                if (nxtvrtx, vrtx) not in edgename:
                    edgename.append((vrtx, nxtvrtx))
        return edgename


#graph_elements = { "a" : ["b","c"],
#                "b" : ["a", "d"],
#                "c" : ["a", "d"],
#                "d" : ["e"],
#                "e" : ["d"]
#                }


graph = Graph()

graph.add_vertex("a")
graph.add_vertex("b")
graph.add_vertex("c")
graph.add_vertex("d")
graph.add_vertex("e")

graph.add_edge(("a" , "b"))
graph.add_edge(("a" , "c"))
graph.add_edge(("b" , "d"))
graph.add_edge(("c" , "d"))
graph.add_edge(("d" , "e"))


print graph.graph
