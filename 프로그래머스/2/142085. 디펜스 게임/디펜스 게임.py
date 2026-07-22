from heapq import heappush, heappop
def solution(n, k, enemy):
    answer = 0
    '''
    1. stage 개수보다 무적권의 개수 k가 같거나 더 많다면 모든 경우에 무적권 사용 가능. stage 길이 반환 
    2. priority queue에 초반 k의 enemy를 저장한다 
    3. q 길이가 k보다 크면, i번째 stage의 enemy[i-1]를 prioru쇼 queue에 저장하고 하나를 pop 한다. pop한 enemy를 남은 병사수 n에서 차감. 차감 실패한다면 i-1 저장 
   '''
    
    stage=len(enemy)
    if k >= stage: 
        return stage
    q=[]
    
    for i in range(stage):
        heappush(q, enemy[i])
        if len(q) > k: 
            last=heappop(q)
            if last > n: 
                return i 
            n-=last 
            
    return stage