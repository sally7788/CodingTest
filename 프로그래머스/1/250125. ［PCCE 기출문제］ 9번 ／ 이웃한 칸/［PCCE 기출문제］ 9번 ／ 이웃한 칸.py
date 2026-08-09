def solution(board, h, w):
    answer = 0
    b_h=len(board)
    b_w=len(board[0])
    visited=[[False]*b_w for _ in range(b_h)]
    dirx=[1,-1,0,0]
    diry=[0,0,1,-1]   

        
    for i in range(4):
        dx=h+dirx[i]
        dy=w+diry[i]

        if dx < 0 or dx >= b_h or dy < 0 or dy >= b_w:
            continue

        if board[h][w]==board[dx][dy]:                
            answer+=1
              
                
    return answer