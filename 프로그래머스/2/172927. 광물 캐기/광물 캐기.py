def solution(picks, minerals):
    '''피로도가 적은 곡갱이를 어디서부터 쓸 것인가? 고민 '''
    answer=float('inf')
    n=len(minerals)
    piro = [
        [1, 1, 1],     # 다이아 곡괭이
        [5, 1, 1],     # 철 곡괭이
        [25, 5, 1]     # 돌 곡괭이
    ]
    
    def mineral_idx(mineral):
        if mineral == "diamond":
            return 0
        elif mineral == "iron":
            return 1
        return 2
    
    def dfs(idx, picks, cost):
        nonlocal answer
        
        if idx >= n or sum(picks)==0:
            answer = min(answer, cost)
            return answer
        
        if cost >= answer: 
            return 
        
        for pick in range(3): #곡갱이 선택
            if picks[pick] == 0: 
                continue
            picks[pick]-=1 #곡갱이 골랐다 
            next_cost=cost
            
            for i in range(idx, min(idx+5, n)): #광물 캐기
                next_cost += piro[pick][mineral_idx(minerals[i])]
            dfs(idx+5,picks,next_cost)
            
            picks[pick]+=1 #원상복구 하는거임... 
    dfs(0,picks[:],0)
            
    
        
            
        
        
    return answer