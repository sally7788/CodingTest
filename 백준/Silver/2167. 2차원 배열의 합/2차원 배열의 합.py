import sys
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[[0]*(m+1)]
for _ in range(n):
    graph.append([0]+list(map(int, input().split())))

psum=[[0] * (m+1) for _ in range(n+1)]
for i in range(n+1):
    for j in range(m+1):
        psum[i][j] = (psum[i-1][j]+psum[i][j-1]-psum[i-1][j-1]+graph[i][j])

k=int(input())

for _ in range(k):
    i,j,x,y=map(int, input().split())
    answer=(psum[x][y]-psum[i-1][y]-psum[x][j-1]+psum[i-1][j-1])
    print(answer)