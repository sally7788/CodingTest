from collections import deque
n=int(input())
for _ in range(n):
    l=int(input())
    x,y=map(int, input().split())
    end_x, end_y=map(int, input().split())

    visited=[[0]*l for _ in range(l)]
    visited[x][y]=1
    
    dirx=[1,1,-1,-1,2,2,-2,-2]
    diry=[2,-2,2,-2,1,-1,1,-1]
    queue=deque()
    queue.append((x,y))

    while queue:
        x,y=queue.popleft()

        if x==end_x and y==end_y:
            print(visited[x][y]-1)
            break
        for i in range(8):
            dx=x+dirx[i]
            dy=y+diry[i]            
        
            if dx < 0 or dy <0 or dx>=l or dy >=l:
                continue
            if visited[dx][dy] == 0:
                visited[dx][dy]=visited[x][y]+1
                queue.append((dx,dy))