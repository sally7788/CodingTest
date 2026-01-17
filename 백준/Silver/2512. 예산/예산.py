import sys

input=sys.stdin.readline

n=int(input())
req=list(map(int, input().split()))
m=int(input())

if sum(req) <= m:
    print(max(req))
    exit()

left=0
right=max(req)
answer=0

while left <= right:
    mid=(left+right)//2
    total=0
    for r in req:
        total+=min(r,mid)
    
    if total <= m:
        answer=mid
        left = mid+1
    elif total > m:
        right = mid -1 
print(answer)    