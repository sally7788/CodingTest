from collections import Counter 
def solution(N, stages):
    answer = []
    
    dic=Counter(stages)
    total_players=len(stages)
    
    for i in range(1,N+1):
        if total_players > 0:
            count=dic[i]
            rate= count/total_players
            answer.append((i, rate))
            
            total_players-=count
        else: 
            answer.append((i,0))
    result=sorted(answer, key=lambda x: (-x[1], x[0]))
    return [s[0] for s in result]