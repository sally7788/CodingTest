from collections import defaultdict, deque
import sys
input = sys.stdin.readline
n=int(input())

x,y=map(int,input().split())

m=int(input())

graph=defaultdict(list)

for _ in range(m):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[-1]*(n+1)

def bfs( start, end):
    
    queue=deque([start])
    visited[start]=0
    
    while queue:
        q=queue.popleft()
        if q==end:
            return visited[q]
        
        for i in graph[q]:
            if visited[i]==-1:
                queue.append(i)
                visited[i]=visited[q]+1
                
    return -1

print(bfs(x, y))