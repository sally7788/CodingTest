from collections import Counter
def solution(k, tangerine):
    answer = 0 
    counts=sorted(Counter(tangerine).values(), reverse=True)
    for c in counts:
        k-=c
        answer+=1
        
        if k <= 0:
            return answer
        
    
    