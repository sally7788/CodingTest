import sys

input=sys.stdin.readline

n,m=map(int, input().split())
p1=0
p2=0
l1=list(map(int, input().split()))
l2=list(map(int, input().split()))
res=[]
while p1 < n and p2 < m:
    if l1[p1] < l2[p2]:
        res.append(l1[p1])
        p1+=1
    else: 
        res.append(l2[p2])
        p2+=1
if p1 < n:
    res.extend(l1[p1:])
if p2 < m:
    res.extend(l2[p2:])    
print(*res)   