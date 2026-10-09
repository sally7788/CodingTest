from itertools import permutations
def solution(k, dungeons):
    answer =-1
    a=k #최초 피로도 
    for dun in permutations(dungeons):
        count=0
        k=a
        for need, cost in dun:
            if need <= k: 
                count+=1
                k-=cost
            else: 
                break 
        answer=max(answer,count)
    return answer