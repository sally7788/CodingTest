def solution(triangle):
    answer = 0
    mm=[[-1]*len(row) for row in triangle]
    
    def dp(i,j): # i,j 까지 왔을 때의 최대 합 
        if i==0 and j==0:
            return triangle[i][j]
        
        if mm[i][j] != -1: #있으면 
            return mm[i][j]  #기존 값 쓰세염 
        
        else: # 기존 값을 어떻게 채우냐면 
            if j==0: 
                mm[i][j]=dp(i-1,0)+triangle[i][j]
            elif j==i: # 맨 오른쪽
                mm[i][j]=dp(i-1,j-1)+triangle[i][j]
            else: 
                mm[i][j] = triangle[i][j] + max(dp(i-1,j), dp(i-1,j-1))
        return mm[i][j]
    
    
                                               
    n=len(triangle)
    answer=max(dp(n-1,j) for j in range(n))
    return answer
