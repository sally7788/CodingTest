import sys
sys.setrecursionlimit(100000) 
input = sys.stdin.readline

n=int(input().strip())

graph=[]
for _ in range(n):
    graph.append(list(input().strip()))

dirx=[1,0,0,-1]
diry=[0,-1,1,0]

def dfs(x,y):
    visited[x][y]=True 
    cur_color=graph[x][y]

    for i in range(4):
        dx=x+dirx[i]
        dy=y+diry[i]
        
        if 0<=dx<n and 0<=dy<n:
            if not visited[dx][dy] and graph[dx][dy] == cur_color:            
                dfs(dx,dy)
            
cnt_normal=0
visited=[[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i,j)
            cnt_normal+=1

visited=[[False]*n for _ in range(n)]
cnt_blind=0

for i in range(n):
    for j in range(n):
        if graph[i][j]=='G':
             graph[i][j]='R'

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i,j)
            cnt_blind+=1

print(cnt_normal, cnt_blind)