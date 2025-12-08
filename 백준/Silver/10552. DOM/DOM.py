import sys
input=sys.stdin.readline

n,m,p=map(int, input().split())

hate=[-1]*(m+1) #그 채널을 싫어하는 사람 중 가장 젊은 사람이 좋아하는 채널 

for _ in range(n):
    a,b=map(int,input().split())
    if hate[b] == -1:
        hate[b]=a
visited=[False]*(m+1)

count=0
current=p

while True:
    if visited[current]:
        print(-1)
        break

    visited[current]=True
    nxt=hate[current]

    if nxt==-1:
        print(count)
        break 

    count+=1
    current=nxt