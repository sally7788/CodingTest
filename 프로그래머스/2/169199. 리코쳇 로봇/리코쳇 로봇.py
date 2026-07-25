from collections import deque
def solution(board):
    answer = float('inf')
    #벽이나 장애물에 부딪힐 때까지 무한 반복 
    queue=deque() #위치, 이동횟수 
    h,w=len(board), len(board[0])
    for i in range(h):
        for j in range(w):
            if board[i][j]== "R":
                rx,ry=i,j
                break 
    queue = deque([(rx, ry, 0)])
    visited=[[False]*w for _ in range(h)]
    visited[rx][ry]=True
    dirx=[1,-1,0,0]
    diry=[0,0,1,-1]
    
    while queue:
        x,y,m=queue.popleft()
        
        if board[x][y]=="G":
                return m
        
        for i in range(4):
            dx,dy=x,y
            while True: 
                ddx=dx+dirx[i]
                ddy=dy+diry[i]
                if not (0 <= ddx < h and 0 <= ddy < w) or board[ddx][ddy] == 'D':
                    break
                dx,dy=ddx,ddy
                    
            if not visited[dx][dy]:
                visited[dx][dy]=True
                queue.append((dx,dy,m+1))
            
    return -1