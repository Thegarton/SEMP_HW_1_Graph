from Graph import wighted_graph

def dfs(g, start, visited):
    visited.add(start)
    stack = [start]
    while stack:
        now = stack.pop()
        for next, w in g.adjList[now]:
            if next not in visited:
                visited.add(next)
                stack.append(next)

def wight(g,comp):
    s = 0
    for k in comp:
        for _, w in g.adjList[k]:
            s+=w
    return s

N, M = map(int, input().split())
edges = []
for i in range(M):
    s = tuple(map(int, input().split()))
    edges.append(s)
g = wighted_graph(edges, N)

new_visited = []
visited = set()
for i in range(N):
    comp = set()
    if i not in visited:
        dfs(g, i, comp)
        visited.update(comp)
        new_visited.append(comp)

w = sorted([wight(g,i) for i in new_visited])

print(w)


