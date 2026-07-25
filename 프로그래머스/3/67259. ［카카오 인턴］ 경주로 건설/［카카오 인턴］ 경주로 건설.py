from collections import deque
def solution(board):
    
    '''
    1.코너인지 아닌지 확인하는 함수 필요 
        1-1.그 전 증가 방향을 알아야돼
        1-2. 그 전 증가 방향과 지금 방향이 달라진 걸 알면.. 코너다
    2. 도로 비용을 계산하면서 bfs를 해야겠는데.... 
    3. dir를 큐에 넣으면 되겠다 
    '''
    
    INF=float('inf')
    w=len(board)
    cost=[[[INF]*4 for _ in range(w)] for _ in range(w)]
    
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]    
    
    money=0
    queue=deque()
    
    for d in range(4):
        cost[0][0][d]=0
        queue.append((0,0,d,0))
    
    while queue: 
        x,y,d,c=queue.popleft()

        for nd in range(4):
            nx=x+dx[nd]
            ny=y+dy[nd]
            
            if nx < 0 or nx >=w or ny < 0 or ny>=w:
                continue
                
            if board[nx][ny]==1:
                continue
            if d == nd:
                nc=c+100
            else:
                nc=c+600
                
            if cost[nx][ny][nd] > nc:
                cost[nx][ny][nd]=nc
                queue.append((nx,ny,nd,nc))
            
    return min(cost[w-1][w-1])