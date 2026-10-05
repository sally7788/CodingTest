def solution(number, limit, power):
    answer = 0
    #약수 개수 구하고
    # 약수 개수가 limit보다 크면 power로 변겨하고 
    #그 모든 값들을 다 합치면 answer 
    
    def yaksu(n):
        count=0
        for i in range(1, int(n**0.5) +1):
            if n % i == 0:
                count+=2
        if int(n**0.5) **2 == n: 
                count-=1
        return count 
    
    for p in range(1,number+1):
        cnt=yaksu(p)
        if cnt > limit:
            answer+=power
        else: 
            answer+=cnt
                
        
    return answer