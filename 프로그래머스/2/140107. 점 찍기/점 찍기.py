def solution(k, d):
    answer = 0
    
    for i in range(d//k+1):
        x=i*k
        max_y=(d**2-x**2)**0.5
        max_j=max_y//k
        answer+=(max_j+1)

    return answer