class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    # Funcion para agregar vertice
    def add_edge(self, u, v, w=1):
        # where w is the weight of the edge
        self.graph[u][v] = w
        self.graph[v][u] = w

    def dfs(self, v, visited):
        visited[v] = True
        print(v, end=' ')
        for i in range(self.V):
            if self.graph[v][i] == 1 and not visited[i]:
                self.dfs(i, visited)

    def dfs_init(self, v):
        visited = [False]*self.V
        self.dfs(v, visited)

# Create a graph given in the above diagram
g = Graph(5)

g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(2, 3)
g.add_edge(3, 3)

g.dfs_init(1)
