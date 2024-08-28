graph = {
    'A': {'B', 'F'},
    'B': {'A', 'C', 'E', 'F'},
    'C': {'B', 'D'},
    'D': {'C', 'F'},
    'E': {'B', 'F'},
    'F': {'A', 'B', 'D', 'E'}
}

def adyacentes(v):
    return graph[v]

def visit(ady, s, parent, colors):
    available_color = 0
    adyacent_colors = []
    for v in ady:
        if v not in parent:
            parent[v] = s
            visit(adyacentes(v), v, parent, colors)

        if v in colors: # detects the correct color based on how many adyacentes colored nodes it has when backtraking
            adyacent_colors.append(colors[v])

    while available_color in adyacent_colors:
        available_color += 1
    colors[s] = available_color

def color_dfs(grafo):
    parent = {}
    colors = {}
    for s in grafo:
        if s not in parent:
            parent[s] = None
            visit(adyacentes(s), s, parent, colors)
    return colors

color_dfs(graph)