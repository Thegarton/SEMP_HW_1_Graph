from collections import defaultdict

def dfs(Graph, start, visited = None):
    if visited is None:
        visited = set()

    visited.add(start)

    for next in Graph[start] - visited:
        dfs(Graph, next, visited)
    return visited

N = int(input())
M = int(input())
Graph = defaultdict(set)

for i in range(M):
    s = list(map(int, input().split()))
    Graph.update({s[0]: set(s[1:])})

if len(Graph) != 0:
    vis = len(dfs(Graph, 0))
    if vis < N:
        print("NO")
    else:
        print("YES")

