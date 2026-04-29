from collections import defaultdict

def solution(n, computers):
    answer = 0
    graph=defaultdict(list)
    for i in range(n):
        for j in range(n):
            if computers[i][j]==1 and i != j :
                graph[i].append(j)
    visited=[False]*n
    def dfs(c):
        visited[c]=True
        for i in range(n):
            if computers[c][i]==1 and not visited[i]:
                dfs(i)
                
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer+=1
        
    return answer