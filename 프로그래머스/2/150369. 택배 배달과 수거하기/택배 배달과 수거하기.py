def solution(cap, n, deliveries, pickups):
    answer=0
    '''
    1. 먼 것부터 배달하고,,
    2. 오는 길에 가져온다 
    '''
    deli=0 # 그 집의 배달개수 
    pick=0
    
    for i in range(n-1,-1,-1):
        deli+=deliveries[i]
        pick+=pickups[i]
        
        while deli > 0 or pick > 0:# 해당 집에 배달, 수거할 택배가 남아 있어 추가로 방문해야함 
            deli -= cap
            pick-=cap
            answer+=(i+1)*2 # 왕복 
            
            
        
            
           
            
    return answer