def solution(money):
    n=len(money)
    
    #마지막 집 제외 
    dp1=[0]*n #0~i번째 집까지 고려했을 때 얻을 수 있는 최대 금액 
    dp1[0]=money[0]
    dp1[1]=max(money[0], money[1])
    
    for i in range(2, n-1):
        dp1[i]=max(dp1[i-1], dp1[i-2]+money[i])
    
    #첫 집 제외 
    dp2=[0]*n
    dp2[1]=money[1]
    dp2[2]=max(money[1], money[2])
    
    for i in range(3, n):
        dp2[i]=max(dp2[i-1], dp2[i-2]+money[i])
    return max(dp1[n-2], dp2[n-1])