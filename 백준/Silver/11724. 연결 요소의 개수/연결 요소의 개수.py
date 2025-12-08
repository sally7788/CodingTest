from collections import deque, defaultdict
import sys
sys.setrecursionlimit(10**6)

input=sys.stdin.readline
def dfs(start, visited):
    stack=deque()
    stack.append(start)
    while stack:
        v=stack.pop()
        if not visited[v]:
            visited[v]=True
            for u in graph[v]:
                if not visited[u]:
                    stack.append(u)

n,m=map(int, input().split())

graph=defaultdict(list)
visited=[False]*(n+1)
count=0

for _ in range(m):
    u,v=map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for node in range(1,n+1):
    if not visited[node]:
        dfs(node, visited)
        count+=1
print(count)