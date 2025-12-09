import sys 

input=sys.stdin.readline
n= int(input())

graph=[]

for _ in range(n):
    graph.append(list(map(int,input().split())))

visited=[0]*n
def dfs(current):
    for next in range(n):
        if graph[current][next] == 1 and visited[next]==0:
            visited[next]=1
            dfs(next) 
    

for i in range(n):
    visited=[0]*n
    dfs(i)
    print(*visited)
