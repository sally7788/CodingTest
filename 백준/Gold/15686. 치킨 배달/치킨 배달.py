from itertools import combinations
import sys

input=sys.stdin.readline
n,m=map(int, input().split())
graph=[]
combi=[]
house=[]

for i in range(n):
    row=list(map(int, input().split()))
    graph.append(row)
    for j in range(n):
        if row[j]==2:
            combi.append((i,j))
        if row[j]==1:
            house.append((i,j))
             

chicken=list(combinations(combi, m))
answer=[]

for i in chicken:
    final_dis=0 #도시 최소 거리 
    for x,y in house:          
        if graph[x][y]==1:
                dis=float('inf')
                for j in range(m):#치킨 1개          
                    dis=min(dis,abs(i[j][0]-x)+abs(i[j][1]-y))
                final_dis+=dis
    answer.append(final_dis)

print(min(answer))