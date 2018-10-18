from  weighted_graph import Graph  , Node

class Dijkstra(object):
    def __init__(self , graph , source , destination):
        self.graph = graph
        self.source = source
        self.destination = destination
        self.source.distance = 0
        self.visited = []
        self.begin()
    def getShortestPath(self):
        return self.visited
    def begin(self , src = None):
        if not src:
            src = self.source
        edges = self.graph.getEdges(src)
        for node in self.visited:
            edges = filter(lambda edge: node not in edge.nodes , edges)
        if(src not in self.visited):
            self.visited.append(src)
            for edge in edges:
                new_dist =  edge.weight + src.distance
                nodeIndex = [i for i , x in enumerate(edge.nodes) if edge.nodes[i] != src][0]
                if(not edge.nodes[nodeIndex].distance):
                    edge.nodes[nodeIndex].distance = new_dist
                elif edge.nodes[nodeIndex].distance > new_dist:
                    edge.nodes[nodeIndex].distance = new_dist
        if(src == self.destination):
            return
        next = self.getMinimum(src , edges)
        self.begin(next)
    def getMinimum(self , src , edges):
        minimum = edges[0]
        if (minimum.nodes[0] == src):
            minimum = minimum.nodes[1]
        else:
            minimum = minimum.nodes[0]
        for edge in edges:
            nodeIndex = [i for i , x in enumerate(edge.nodes) if edge.nodes[i] != src][0]
            if edge.nodes[nodeIndex].distance < minimum.distance:
                minimum = edge.nodes[nodeIndex]
        return minimum




myGraph = Graph()
vertices = [Node("A") , Node("B") , Node("C") , Node("D") , Node("E") , Node("F")]

for vertex in vertices:
    myGraph.add_vertex(vertex)

edges = [
    #A -> B                               #A -> C                       #A -> D
    ((vertices[0] , vertices[1]) , 2) , ((vertices[0] , vertices[2]) , 5) , ((vertices[0] , vertices[3]) , 1) ,
    #B -> C                                #B -> D
    ((vertices[1] , vertices[2]) , 3) , ((vertices[1] , vertices[3]) , 2) ,
    #C -> D                                    #C -> E                       #C -> F
    ((vertices[2] , vertices[3]) , 3) , ((vertices[2] , vertices[4]) , 1) , ((vertices[2] , vertices[5]) , 5),
    #D -> E
    ((vertices[3] , vertices[4]) , 1),
    #E -> F
    ((vertices[4] , vertices[5]) , 2)
    ]

for edge in edges:
    myGraph.add_edge(edge[0] , edge[1])


source = vertices[0]
destination = vertices[5]

print Dijkstra(myGraph , source , destination).getShortestPath()
