class Vertex:
    def __init__(self, key, neightbors = []):
        self.id = key
        self.connectedTo = neightbors
        self.visited = False

    def addNeighbor(self, neighbor):
        self.connectedTo.append(neighbor)

    def getAdj(self):
        return self.connectedTo

    def setVisited(self, visited):
        self.visited = visited

    def getVisited(self):
        return self.visited

    def __repr__(self):
        return self.id

def dfs(vertex):
    for v in vertex.getAdj():
        if v.getVisited() == False:
            v.setVisited(True)
            print(v)
            dfs(v)

vs = [Vertex("B"), Vertex("C"), Vertex("D"), Vertex("E"), Vertex("F")]
v0 = Vertex("A", vs)

dfs(v0)