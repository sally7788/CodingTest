from itertools import combinations
from collections import deque
n,m=map(int, input().split())
graph=[list(map(int, input().split())) for _ in range(n)]

blanks, virus=[],[]
max_safe=0

for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            blanks.append((i,j))
        if graph[i][j]==2:
            virus.append((i,j))

cand_list=combinations(blanks,3)
dx=[1,-1,0,0]
dy=[0,0,1,-1]
for col in cand_list:
    temp_graph=[row[:] for row in graph]

    #새로운 그래프 그리기     
    for i in range(3):
        x,y=col[i]
        temp_graph[x][y]=1

    #바이러스 확산하기     
    queue=deque(virus)      
    while queue:
        vx,vy=queue.popleft()

        for i in range(4):
            nx=vx+dx[i]
            ny=vy+dy[i]

            if 0<=nx<n and 0 <= ny < m and temp_graph[nx][ny]==0:                
                temp_graph[nx][ny]=2
                queue.append((nx,ny))
    cnt = sum(row.count(0) for row in temp_graph)
    max_safe=max(max_safe, cnt)
print(max_safe)