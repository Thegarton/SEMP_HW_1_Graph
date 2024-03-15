from Graph import orgraph
ans = []

# поиск в глубину
def dfs(vertex, visited, order):
    visited[vertex] = 1
    for u in g.adjList[vertex]:
        if(visited[u] == 0):
            dfs(u, visited.copy(), order)
    if vertex not in order:
        order.append(vertex)

# проверка на ацикличность
def cycle(vertex, color, visited_steck = None):
    if visited_steck == None:
        visited_steck = []

    color[vertex] = 1
    visited_steck.append(vertex)

    for u in g.adjList[vertex]:
        if(color[u] == 0):
            cycle(u, color.copy(), visited_steck.copy())
        if color[u] == 1:
            ans.append(visited_steck)

    color[vertex] = 2

N, M = map(int, input().split())
visited = [0 for _ in range(N)]
edges = []
for i in range(M):
    s = tuple(map(int, input().split()))
    edges.append(s)
g = orgraph(edges, N)
order = []


for i in range(N):
    color = [0 for _ in range(N)]
    if color[i] == 0:
        cycle(i, color)

if len(ans) == 0:
    for i in range(N):
        visited = [0 for _ in range(N)]
        if visited[i] == 0:
            c = dfs(i,visited, order)

    print(order[::-1])
else:
    print("NO")
