
from collections import deque
r,c=map(int, input().split())

graph=[]
dirx=[1,-1,0,0]
diry=[0,0,-1,1]
water=[]

for i in range(r):
    row=list(input())
    graph.append(row)
    for j in range(c):
        if graph[i][j]=="*":
            water.append((i,j))
        if graph[i][j]=="S":
            s_place=(i,j)

water_time=[[-1]*c for _ in range(r)]

def water_dfs():
    queue=deque()
    for a,b in water:        
        queue.append((a,b))
        water_time[a][b]=0

    while queue:
        x,y=queue.popleft()

        for i in range(4):
            dx=x+dirx[i]
            dy=y+diry[i]

            if dx<0 or dy<0 or dx>=r or dy>=c:
                continue
            if graph[dx][dy]=="D" or graph[dx][dy]=="X":
                continue
            if water_time[dx][dy]== -1:
                water_time[dx][dy]=water_time[x][y]+1
                queue.append((dx,dy))

visited=[[-1]*c for _ in range(r)]

def d_bfs(a,b):
    queue=deque([(a,b)])
    visited[a][b]=0
    
    while queue:
        x,y=queue.popleft()

        if graph[x][y]=="D":
            return visited[x][y]
           
        for i in range(4):
            dx=x+dirx[i]
            dy=y+diry[i]

            if dx<0 or dy<0 or dx>=r or dy>=c:
                continue
            if graph[dx][dy]=="*" or graph[dx][dy]=="X":
                continue
            if visited[dx][dy]== -1:
                next_time=visited[x][y]+1
                if water_time[dx][dy]==-1 or next_time < water_time[dx][dy]:
                    visited[dx][dy]=next_time
                    queue.append((dx,dy))
    return "KAKTUS"
water_dfs()
print(d_bfs(s_place[0],s_place[1]))