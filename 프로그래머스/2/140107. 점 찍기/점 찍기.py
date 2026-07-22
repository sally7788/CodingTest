def solution(k, d):
    answer = 0
    for i in range(0, d//k+1):
        x=i*k 
        max_y=(d**2-x**2)**0.5
        max_j=max_y//k #y가 몇번 들어갔는지 y=j*k의 j의 최댓값 
        answer+=(max_j+1)
        
    return answer
