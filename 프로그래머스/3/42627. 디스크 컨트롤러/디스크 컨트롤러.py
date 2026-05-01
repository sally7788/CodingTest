import heapq 
def solution(jobs):
    jobs.sort()
    answer = 0
    heap=[]
    t=0
    i=0
    total=0
    n=len(jobs)
    
    while i < n or heap:
        
        while i < n and jobs[i][0] <= t:
            start, work = jobs[i]
            heapq.heappush(heap, (work, start))
            i+=1
        if heap: 
            work, start=heapq.heappop(heap)
            t+=work 
            total+=(t-start)
        else: # 일 없으면 시간 점프 
            t=jobs[i][0]
    return total // n
    
        
        
        
        
  