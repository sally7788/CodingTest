n,m=map(int, input().split())
r,c,d=map(int, input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int, input().split())))


dirx=[-1,0,1,0] #북,동,남,서 
diry=[0,1,0,-1]
cnt=0
while True:
    if graph[r][c]==0:
        graph[r][c]=2
        cnt+=1
    found=False

    for _ in range(4):
        d=(d+3) % 4
        nx,ny=r+dirx[d], c+diry[d]
        
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny]==0: 
            r,c=nx,ny
            found=True
            break
    if not found:
        bx,by=r-dirx[d],c-diry[d]

        if 0 <= bx < n and 0 <= by < m and graph[bx][by] != 1:
            r,c=bx,by
        else:
            break 
print(cnt)    
  
