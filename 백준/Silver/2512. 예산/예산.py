n=int(input())
req=list(map(int,input().split()))
m=int(input())

left=0
right=max(req)
answer=0
if sum(req) <= m:
    print(max(req))
    exit()
else:
    while left <= right:
        mid=(left+right)//2
        budget=0
        for r in req:
            budget+=min(mid,r)
        if budget > m:
            right=mid-1
        if budget <= m:
            answer=mid
            left=mid+1
print(answer)