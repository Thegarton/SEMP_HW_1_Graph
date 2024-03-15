from collections import deque
from Graph import graph_nor
class cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

import numpy as np
def BFS(s, t):
    dis = [[-1]*(M+2) for _ in range(N+2)]
    dis[s.x][s.y] = 0
    q = deque([s])
    while(q):
        c = q.popleft()
        x = c.x
        y = c.y
        if x + 1 <= N+1 or y + 1 <= M+1:
            for dx, dy in [[-1, 0], [1,0], [0, -1], [0, 1]]:
                _x = x + dx
                _y = y + dy
                if( maze[_x][_y] and dis[_x][_y] != -1):
                    continue
                elif( maze[_x][_y] and dis[_x][_y] == -1):
                    dis[_x][_y] = dis[x][y] + 1
                    q.append(cell(_x, _y))
    return dis
N, M = map(int, input().split())
x_s, y_s = map(int, input().split())
x_t, y_t = map(int, input().split())

cell_s = cell(x_s+1, y_s+1)
cell_t = cell(x_t+1, y_t+1)

maze = []
first = [ 0 for _ in range(M+2)]
maze.append(first)
for _ in range(N):
    str = list('X'+input()+'X')
    for i in range(len(str)):
        if str[i] == 'X':
            str[i] = 0
        else:
            str[i] = -1
    maze.append(str)

maze.append(first)
print(np.shape(maze))
dis = BFS(cell_s,cell_t)
print(dis)
if dis[cell_t.x][cell_t.y] == -1:
    print('INF')
else:
    print(dis[cell_t.x][cell_t.y])
