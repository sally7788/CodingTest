import math
import sys
input=sys.stdin.readline
n= int(input())
m=int(input())
place=list(map(int,input().split()))

side=[place[i+1]-place[i] for i in range(m-1)]

if not side:
    max_side=0
else: 
    max_side=max(side)
left=0
right=n

while left <= right:
    mid=(left+right)//2
    
    if mid >= place[0] and mid >= (n-place[-1]) and mid >= (max_side+1)//2:
        answer=mid 
        right = mid-1
    else:
        left=mid+1

print(answer)
    