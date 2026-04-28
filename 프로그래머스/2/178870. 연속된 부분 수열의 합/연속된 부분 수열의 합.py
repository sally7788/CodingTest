def solution(sequence, k):
    # 1. 합이 k이고 연속된 수열을 찾는다. 
    # 2. 길이가 가장 짧은 수열을 찾는다 
    # 3. 그 중에서 앞에 있는 시작,끝 인덱스를 반환한다
    left,total,answer=0,0,[]
    min_len=float('inf')
    
    for right in range(len(sequence)):
        total+=sequence[right]
        
        while total > k:
            total -= sequence[left]
            left+=1
        
        if total == k:
            if right-left < min_len:
                min_len = right-left
                answer=[left, right]
    
            
                
            
    
    return answer