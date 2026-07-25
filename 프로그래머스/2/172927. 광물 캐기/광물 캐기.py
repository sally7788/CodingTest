def solution(picks, minerals):
    answer = float('inf')
    n=len(minerals)
    def minerals_change(mineral):
        if mineral=="diamond":
            return 0
        if mineral=="iron":
            return 1
        else: return 2 
    
    piro=[[1,1,1],[5,1,1],[25,5,1]]
    cost=0
    def dfs(idx, picks, cost):
        nonlocal answer 
        
        if idx >= n or sum(picks)==0:
            answer=min(answer, cost)
            return answer 
        
        if cost >= answer: 
            return 
        
        for i in range(3):
            if picks[i] ==0 : 
                continue
            picks[i]-=1
            next_cost=cost
            
            for j in range(idx, min(idx+5, n)):
                next_cost+=piro[i][minerals_change(minerals[j])]
            dfs(idx+5, picks, next_cost)
            
            picks[i]+=1
    dfs(0, picks[:],0)
    return answer