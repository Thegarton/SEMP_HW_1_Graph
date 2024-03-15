from Graph import graph_no_or_AP

N, M = map(int, input().split())
visited = [0 for _ in range(N)]
edges = []
for i in range(M):
    s = tuple(map(int, input().split()))
    edges.append(s)
g = graph_no_or_AP(edges, N+1)
g.AP()