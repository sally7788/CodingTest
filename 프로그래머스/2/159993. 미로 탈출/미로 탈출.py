from collections import deque
def bfs(start, end, maps):
    w=len(maps)
    h=len(maps[0])
    visited=[[False]*h for _ in range(w)]
    
    queue=deque()
    sx,sy=start
    ex,ey=end 
    
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    
    queue.append((sx,sy,0))
    visited[sx][sy]=True
    
    while queue:
        x,y,dist=queue.popleft()
        
        if (x,y)==(ex,ey):
            return dist

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0 <= nx < w and 0 <= ny < h:
                if maps[nx][ny] !='X' and not visited[nx][ny]:
                    visited[nx][ny]=True
                    queue.append((nx,ny,dist+1))
    return -1            
    
def solution(maps):
    w, h = len(maps), len(maps[0])
    
    # S, L, E 위치 찾기
    for i in range(w):
        for j in range(h):
            if maps[i][j] == 'S':
                S = (i, j)
            elif maps[i][j] == 'L':
                L = (i, j)
            elif maps[i][j] == 'E':
                E = (i, j)
    dist1=bfs(S,L,maps)
    if dist1==-1:
        return -1
    dist2=bfs(L,E,maps)
    if dist2==-1:
        return -1
    return dist1+dist2
            
    
    
    

    
    return -1