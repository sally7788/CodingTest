def time_calc(diffs, times, level):
    tot_time=0
    for i,d in enumerate(diffs):
        if level >= d:
            t=times[i]
        else: 
            t=(d-level)*(times[i]+times[i-1])+times[i]
        tot_time+=t
    return tot_time    
            
def solution(diffs, times, limit):
    # answer = inf(float)
    left=min(diffs)
    right=max(diffs)    
       
    while left <= right:
        mid=int((left+right)//2)
        tot_time = time_calc(diffs, times, mid)
        
        if tot_time > limit: 
            left=mid+1
        else: 
            right=mid-1
    
    
    return left

print(int(8.6))