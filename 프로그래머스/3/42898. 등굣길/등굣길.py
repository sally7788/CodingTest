def solution(m, n, puddles):
    answer = 0
    # 이게 왜 디피야 
    # 물의 i-1,j+1 / i+1,i-1까지 도착하는거 + 그 이후에는 같으니까... 물이 여러개 있어도,,,,, 아 풀기존나싫어 아~~~~~~~~~~~~~~~~~~~~~~~~~~~
    puddles=[[q,p] for [p,q] in puddles]
    dp=[[0]*(m+1) for i in range(n+1)]
    
    dp[1][1]=1
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==1 and j==1: continue
            if [i,j] in puddles:
                dp[i][j]==0
            else: 
                dp[i][j]=(dp[i-1][j]+dp[i][j-1])%1000000007
    return dp[n][m]