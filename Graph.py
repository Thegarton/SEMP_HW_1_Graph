class wighted_graph:
    def __init__(self, edges, n):
        self.adjList = [ set() for _ in range(n)]
        for (start, end, wight) in edges:
            self.adjList[start].add((end,wight))
    def __len__(self):
        return len(self.adjList)

class graph_nor:
    def __init__(self, edges, n):
        self.adjList = [ set() for _ in range(n)]
        for (start, end) in edges:
            self.adjList[start].add(end)
    def __len__(self):
        return len(self.adjList)


class orgraph:
    def __init__(self, edges, n):
        self.adjList = [ set() for _ in range(n)]
        for (start, end) in edges:
            self.adjList[start].add(end)
    def __len__(self):
        return len(self.adjList)

class graph_no_or_AP:
    def __init__(self, edges, n):
        self.N = n
        self.adjList = [set() for _ in range(n)]
        self.Time = 0
        for (start, end) in edges:
            self.adjList[start].add(end)

    def __len__(self):
        return len(self.adjList)

    def APUtil(self, u, visited, ap, parent, low, disc):

        children = 0

        visited[u] = True

        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1

        for v in self.adjList[u]:
            if visited[v] == False:
                parent[v] = u
                children += 1
                self.APUtil(v, visited, ap, parent, low, disc)

                low[u] = min(low[u], low[v])

                if parent[u] == -1 and children > 1:
                    ap[u] = True

                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True

            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    def AP(self):
        visited = [False] * (self.N)
        disc = [float("Inf")] * (self.N)
        low = [float("Inf")] * (self.N)
        parent = [-1] * (self.N)
        ap = [False] * (self.N)

        for i in range(self.N):
            if visited[i] == False:
                self.APUtil(i, visited, ap, parent, low, disc)
        ans = []
        for index, value in enumerate(ap):
            if value == True: ans.append(index)

        if len(ans) == 0:
            print(-1)
        else:
            print(*ans)

