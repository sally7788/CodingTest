from collections import deque
def solution(maps):
    answer = []
    h=len(maps)
    w=len(maps[0])
    visited=[[False]*w for _ in range(h)]
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    
    def bfs(x,y):
        total=int(maps[x][y])
        queue=deque([(x,y)])
        while queue:  #한 덩어리를 탐색 
            nx,ny=queue.popleft()
            
            for i in range(4):
                cx=dx[i]+nx
                cy=dy[i]+ny
            
                if cx < 0 or cx >= h or cy < 0 or cy >=w:
                    continue 

                if not visited[cx][cy] and maps[cx][cy] != "X":
                    visited[cx][cy]=True
                    total+=int(maps[cx][cy])
                    queue.append((cx,cy))
        return total
       
    for i in range(h):
        for j in range(w):         
            if not visited[i][j] and maps[i][j] != "X":
                visited[i][j]= True             
                answer.append(bfs(i,j))
        
    return sorted(answer) if answer else [-1]