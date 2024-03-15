from collections import deque
from Graph import graph_nor
class cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

import numpy as np
def BFS(s, t):
    dis = [[-1]*(M+2) for _ in range(N+2)]
    dis[s.x+1][s.y+1] = 0
    q = deque([])
    print(np.shape(dis))
    while(q):
        c = q.popleft()
        print(c.x,c.y)
        x = c.x + 1
        y = c.y + 1
        if x + 1 <= N+1 or y + 1 <= M+1:
            for dx, dy in [[-1, 0], [1,0], [0, -1], [0, 1]]:
                print(dx, dy)
                _x = x + dx
                _y = y + dy
                if( maze[_x][_y] and dis[_x][_y] != -1):
                    continue
                elif( maze[_x][_y] and dis[_x][_y] != -1):
                    dis[_x][_y] = dis[x][y] + 1
                    q.append(cell(_x, _y))
    print(dis)
N, M = map(int, input().split())
x_s, y_s = map(int, input().split())
x_t, y_t = map(int, input().split())

cell_s = cell(x_s, y_s)
cell_t = cell(x_t, y_t)

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
BFS(cell_s,cell_t)
