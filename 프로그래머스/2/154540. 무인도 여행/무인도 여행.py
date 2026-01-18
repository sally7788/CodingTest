from collections import deque 
def solution(maps):
    
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    visited=[[False]*len(maps[0]) for _ in range(len(maps))]
    
    def dfs(x,y):
        queue=deque([(x,y)])
        total=int(maps[x][y])
        visited[x][y]=True 
        
        while queue: 
            x,y=queue.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]

                if 0 <=nx < len(maps) and 0 <=ny < len(maps[0]):                    
                    if maps[nx][ny] != 'X' and not visited[nx][ny]:
                        visited[nx][ny]=True
                        total+=int(maps[nx][ny])
                        queue.append((nx,ny))       
        return total
    result=[]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] !='X' and not visited[i][j]:
                result.append(dfs(i,j))
    return sorted(result) if result else [-1]
        
            
    