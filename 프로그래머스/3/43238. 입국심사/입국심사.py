def solution(n, times):
    
    left=0
    right=max(times)*n
    
    while left <= right: 
        total=0
        mid=int((left+right)//2) #시간 
        
        for t in times: 
            total +=mid//t
        if total >= n: 
            right=mid-1
        else: 
            left=mid+1
        
        
    return left