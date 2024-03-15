from collections import deque
from Graph import graph_nor

def bfs(s, N):
    distance = [-1] * (N)
    distance[s] = 0
    q = deque([s])
    while q:
        s = q.popleft()
        for neighbor in g.adjList[s]:
            if distance[neighbor] != -1:
                continue
            distance[neighbor] = distance[s] + 1
            q.append(neighbor)
    return distance

N, M = map(int, input().split())
edges = []

for i in range(M):
    s = list(map(int, input().split()))
    s = sorted(s)
    edges.append(s)
g = graph_nor(edges, N)
d = bfs(0, N)

for i in d:
    print(i)