def solution(clothes):
    answer = 1
    
    clot={}
    for c,k in clothes:
        clot[k]=clot.get(k, 0)+1
    
    for k,v in clot.items():
        answer *= (v+1)
    
    
    return answer-1