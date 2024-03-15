from Graph import orgraph
ans = []

def dfs(vertex, color, visited_steck = None):
    if visited_steck == None:
        visited_steck = []

    color[vertex] = 1
    visited_steck.append(vertex)

    for u in g.adjList[vertex]:
        if(color[u] == 0):
            dfs(u, color.copy(), visited_steck.copy())
        if color[u] == 1:
            ans.append(visited_steck)

    color[vertex] = 2

N, M = map(int, input().split())
color = [0 for _ in range(N)]
edges = []

for i in range(M):
    s = tuple(map(int, input().split()))
    edges.append(s)

g = orgraph(edges, N)
for i in range(N):
    color = [0 for _ in range(N)]
    if color[i] == 0:
        dfs(i,color)

if len(ans) == 0:
    print("YES")

else:
    ans = sorted(ans, key=len)
    print()
    print(ans[0])