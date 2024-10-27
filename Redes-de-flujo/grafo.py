from collections import deque

class Edge:
    def __init__(self, source, target, capacity=0):
        self.source = source
        self.target = target
        self.capacity = capacity
        self.flow = 0

    def get_residual_capacity(self):
        return self.capacity - self.flow

    def __repr__(self):
        return f'{self.source} -> {self.target}'

class Vertex:
    def __init__(self, name):
        self.visited = False
        self.name = name
        self.edges = set()  # List of outgoing edges

    def get_name(self):
        return self.name

    def add_edge(self, edge):
        self.edges.add(edge)

    def get_edges(self):
        return self.edges

    def get_edge_to(self, target):
        for edge in self.edges:
            if edge.target == target:
                return edge
        return None

    def visit(self):
        self.visited = True

    def visited(self):
        return self.visited

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return self.name

class Graph:
    def __init__(self, vertices=None, edges=None):
        self.vertices = set(vertices) if vertices is not None else set()
        self.edges = set(edges) if edges is not None else set()

        # Initialize vertex edge lists from provided edges
        if edges:
            for edge in edges:
                edge.source.add_edge(edge)

    def add_vertex(self, vertex):
        self.vertices.add(vertex)

    def add_edge(self, edge):
        self.edges.add(edge)

    def get_edge(self, source, target):
        return source.get_edge_to(target)

    def set_all_flows(self, flow):
        for edge in self.edges:
            edge.flow = flow

    def augmenting_path(self, s, t):
        if s not in self.vertices or t not in self.vertices:
            return None

        cola = deque([s])
        parent_edge = {s: None}

        while cola:
            actual = cola.popleft()
            if actual.visited:
                continue
            actual.visit()
            for edge in actual.get_edges():
                target = edge.target
                if not target.visited and edge.get_residual_capacity() > 0:
                    parent_edge[target] = edge
                    if target == t:
                        path = []
                        while target:
                            edge = parent_edge[target]
                            if not edge:
                                break
                            path.append(edge)
                            target = edge.source

                        return path[::-1]
                    cola.append(target)

        return None


    def bottle_neck(self, path):
        if len(path) < 1:
            return 0
        b = float('inf')
        for edge in path:
            b = min(b, edge.get_residual_capacity())
        return b

    def augment(self, path):
        b = self.bottle_neck(path) # this is the minimum residual capacity of the path
        for edge in path:
            edge.flow += b
            back_edge = edge.target.get_edge_to(edge.source)
            if back_edge:
                back_edge.flow -= b



class ResidualGraph(Graph):
    def __init__(self, original_graph):
        # Create mapping of original vertices to new vertices
        self.vertex_mapping = {}
        vertices = set()

        # Create new vertices with same names
        for vertex in original_graph.vertices:
            new_vertex = Vertex(vertex.name)
            self.vertex_mapping[vertex] = new_vertex
            vertices.add(new_vertex)

        # Build edges using the new vertices
        residual_edges = self._build_residual_edges(original_graph)
        super().__init__(vertices, residual_edges)

    def _build_residual_edges(self, graph):
        new_edges = set()
        for edge in graph.edges:
            # Get corresponding new vertices
            new_source = self.vertex_mapping[edge.source]
            new_target = self.vertex_mapping[edge.target]

            # Forward edge
            if edge.get_residual_capacity() > 0:
                forward_edge = Edge(new_source, new_target, edge.get_residual_capacity())
                new_source.add_edge(forward_edge)
                new_edges.add(forward_edge)

            # Backward edge
            if edge.flow > 0:
                previous_backward_flow = 0
                previous_backward_edge = edge.target.get_edge_to(edge.source)
                if previous_backward_edge: # this takes into consideration the already existing backward edges
                    previous_backward_flow = previous_backward_edge.flow
                backward_edge = Edge(new_target, new_source, edge.flow + previous_backward_flow)
                new_target.add_edge(backward_edge)
                new_edges.add(backward_edge)

        return new_edges