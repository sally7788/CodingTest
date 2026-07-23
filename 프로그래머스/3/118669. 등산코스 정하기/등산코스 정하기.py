from collections import defaultdict
from heapq import heappop, heappush
def solution(n, paths, gates, summits):
    answer = []
    '''
    1. 내가 선택을 해야되고 
    2. 선택이 다음 선택에 영향을 주고 
    3. 선택할 수 있느 게 너무 많아 -> 그리디, dp가 있는데... 
    3. 작은 문제로 쪼개는 게 의미가 없으니까 그리디로 간다. 가지치기하고
    '''
    graph=defaultdict(list)
    for s,d,e in paths: 
        graph[s].append((d,e))
        graph[d].append((s,e))
    
    def get_min_intensity():
        pq=[]
        visited=[1000000001]*(n+1) #최소 intensity 
        
        for gate in gates:
            heappush(pq, (0,gate))
            visited[gate]=0
        
        #산봉우리 도착할 때까지 반복
        while pq: 
            intensity, node=heappop(pq)
            
            if node in summits_set or intensity > visited[node]:
                continue
            for next_node, energy in graph[node]:
                new_intensity=max(intensity, energy)
                if new_intensity < visited[next_node]:
                    visited[next_node]=new_intensity
                    heappush(pq,(new_intensity, next_node))
        min_intensity=[0,100000001]
        for summit in summits:
            if visited[summit] < min_intensity[1]:
                min_intensity[0]=summit
                min_intensity[1]=visited[summit]
        return min_intensity
    summits.sort()
    summits_set=set(summits)
        
    return get_min_intensity()