graph = [[0, 2, 1, 0, 0, 0, 10], # 0
         [0, 0, 0, 1, 3, 0, 0],  # 1
         [0, 3, 0, 4, 1, 0, 0],  # 2
         [0, 0, 0, 0, 2, 5, 1],  # 3
         [0, 0, 0, 0, 0, 3, 5],  # 4
         [0, 0, 0, 0, 0, 0, 1],  # 5
         [0, 0, 0, 0, 0, 0, 0]]  # 6

def _maxDistance(graph):
    n = len(graph)
    dp = [0] * n
    for i in range(n):
        for j in range(i):
            if graph[j][i] > 0:
                dp[i] = max(dp[i], dp[j] + graph[j][i])
    return dp[-1]

def maxDistance(graph, k, maxCosts): # O(n)
    if k == 0:
        return 0
    from_idxs = [i for i in range(len(graph)) if graph[i][k] != 0]  # O(n)

    for i in from_idxs:
        if maxCosts[i] == 0:
            maxCosts[i] = maxDistance(graph, i, maxCosts)

    return max([maxCosts[i] + graph[i][k] for i in from_idxs])

print(maxDistance(graph, -1, [0] * len(graph)))

