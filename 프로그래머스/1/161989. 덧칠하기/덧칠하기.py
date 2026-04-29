def solution(n, m, section):
    answer=0
    paint=0
    
    for s in section:
        if s > paint:
            answer+=1
            paint=s+m-1
    return answer