def is_valid(graph, v, color, c, vertices):
    return all(u not in color or c != color[u] for u in list(graph[vertices[v]]))

def color_graph(graph, m, color, v, vertices):
    if v == len(vertices):
        return True

    for c in range(1,m+1):
        if is_valid(graph, v, color, c, vertices):
            color[vertices[v]] = c
            if color_graph(graph, m, color, v+1, vertices):
                return True
            color[v] = 0  # this sets the color to 0 for the folllowing attempts to accept a new color (backtracking)
    return False

def optimal_coloring(graph):
    vertices = list(graph.keys())
    for m in range(1,len(graph.keys())+1):
        color = {}
        if color_graph(graph, m, color, 0, vertices):
            return color, m
    return None

graph = {
    'A': {'B', 'F'},
    'B': {'A', 'C', 'E', 'F'},
    'C': {'B', 'D'},
    'D': {'C', 'F'},
    'E': {'B', 'F'},
    'F': {'A', 'B', 'D', 'E'}
}

color, m = optimal_coloring(graph)
print(m)