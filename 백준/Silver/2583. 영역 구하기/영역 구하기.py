import sys
sys.setrecursionlimit(10000)

m,n,k=map(int, input().split())

graph=[[0]*n for _ in range(m)]
visited=[[False]*n for _ in range(m)]

for _ in range(k):
    left_x,left_y,right_x,right_y=map(int, input().split())
    for x in range(left_x, right_x):
        for y in range(left_y, right_y):
            graph[y][x]+=1

dirx=[1,-1,0,0]
diry=[0,0,1,-1]

def dfs(x,y):
    visited[x][y]=True
    size=1

    for d in range(4):
        nx=x+dirx[d]
        ny=y+diry[d]

        if nx < 0 or ny < 0 or nx >=m or ny >= n:
            continue
        if not visited[nx][ny] and graph[nx][ny]==0:
            size+=dfs(nx,ny)
    return size 

answer=[]
for i in range(m):
    for j in range(n):
        if not visited[i][j] and graph[i][j]==0:
            answer.append(dfs(i,j))

answer.sort()
print(len(answer))
print(*answer)


