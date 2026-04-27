import heapq #가장 작은 값 먼저 꺼내는 자료구조 

def solution(N, road, K):
    answer = 0
    graph=[[] for _ in range(N+1)]
    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))
    dist=[float('inf')]*(N+1) #1에서 각 마을까지의 거리 
    dist[1]=0
    
    heap=[(0,1)]
    
    while heap:
        cost, now= heapq.heappop(heap)
        
        if cost > dist[now]:
            continue
        
        for next_node, next_cost in graph[now]:
            new_cost=cost+next_cost
            
            if new_cost < dist[next_node]:
                dist[next_node]=new_cost
                heapq.heappush(heap, (new_cost, next_node))

    return sum(1 for d in dist if d <= K)