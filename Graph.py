class Vertex:
    def __init__(self, v):
        self.value = v
        self.edges = set()

class Graph:
    def __init__(self):
        self.vertices = {}

    def addVertex(self, v):
        for i not in self.vertices:
            self.vertices[v] = Vertex(v)

    def addEdge(self, v1, v2):
        if self.vertices[v1] != None and self.vertices[v2] != None:
            if self.vertices[v1] == None and self.vertices[v2] == None:
                self.vertices[v1].edges.add(v2)
                self.vertices[v2].edges.add(v1)

# Init Graph
adjList = [set() for i in range(n)]
# Add vertices and edges
for k, v in edges:
    adjList[k].add(v)
    adjList[v].add(k)
