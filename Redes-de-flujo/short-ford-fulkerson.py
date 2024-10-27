from collections import deque
from email.policy import default


class Graph:
    def __init__(self, n):
        self.vertices = n
        self.graph = dict()

    def add_edge(self, u, v, capacity):
        self.graph[u] = self.graph.get(u, dict())
        self.graph[u][v] = capacity

    def get_flow_graph(self, residual_graph): # TODO fix
        """Compute the flow graph from the residual graph."""
        flow_graph = Graph(self.vertices)

        for u in self.graph:
            for v, capacity in self.graph[u].items():
                # The flow is the capacity of the reverse edge in the residual graph
                flow = residual_graph.graph[v][u] if v in residual_graph.graph and u in residual_graph.graph[v] else 0
                if flow > 0:
                    flow_graph.add_edge(u, v, flow)

        return flow_graph

    def get_residual_graph(self): # TODO fix
        """Create and return a residual graph."""
        # Create a new graph with the same number of vertices
        residual = Graph(self.vertices)

        # Copy all edges and their capacities
        for u in self.graph:
            for v, capacity in self.graph[u].items():
                residual.graph[u][v] = capacity
                # Initialize reverse edges with 0 capacity if they don't exist
                if v not in self.graph or u not in self.graph[v]:
                    residual.graph[v][u] = 0

        return residual

    def bfs(self, source, sink, parent):
        """Use BFS to find if there's a path from source to sink.
        Also fills parent[] to store the path."""

        # Mark all vertices as not visited
        visited = dict()

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(source)
        visited[source] = True

        # Standard BFS loop
        while queue:
            u = queue.pop(0)

            # Consider all adjacent vertices
            for v in self.graph.get(u, dict()):
                # If vertex is not visited and has capacity
                if not visited.get(v, False) and self.graph[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True

        # Return True if we reached sink in BFS
        return visited.get(sink, False)

    def ford_fulkerson(self, source, sink):
        """Returns the maximum flow from source to sink in the given graph."""

        # Initialize variables
        parent = dict()
        max_flow = 0

        # Augment the flow while there is a path from source to sink
        while self.bfs(source, sink, parent):

            # Find minimum residual capacity of the edges along the
            # path found by BFS
            path_flow = float("inf")
            s = sink
            while s != source:
                actual = parent.get(s, None)
                path_flow = min(path_flow, self.graph[actual][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow += path_flow

            # Update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow # Fordward edge surely exists

                self.graph[v] = self.graph.get(v, dict())
                self.graph[v][u] = self.graph[v].get(u, 0) + path_flow # Backward edge (might not exist)

                v = parent[v]

        return max_flow

    def print_graph(self):
        """Print the current state of the graph."""
        for u in self.graph:
            for v in self.graph[u]:
                print(f"Edge {u}->{v}: Capacity = {self.graph[u][v]}")

# Example usage
def example():
    # Create a graph with 6 vertices
    g = Graph(6)

    # Add edges with their capacities
    g.add_edge(0, 1, 16)
    g.add_edge(0, 2, 13)
    g.add_edge(1, 2, 10)
    g.add_edge(1, 3, 12)
    g.add_edge(2, 1, 4)
    g.add_edge(2, 4, 14)
    g.add_edge(3, 2, 9)
    g.add_edge(3, 5, 20)
    g.add_edge(4, 3, 7)
    g.add_edge(4, 5, 4)

    # Find and print the maximum flow
    source, sink = 0, 5
    max_flow = g.ford_fulkerson(source, sink)
    print(f"Maximum flow from vertex {source} to vertex {sink}: {max_flow}")

example()