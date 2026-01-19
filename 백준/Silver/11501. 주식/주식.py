import sys
input=sys.stdin.readline

t=int(input())

for _ in range(t):    

    n=int(input())
    nums=list(map(int,input().split()))

    max_price=0
    profit=0

    for i in range(n-1,-1,-1):
        if nums[i] > max_price:
            max_price=nums[i]
        else:
            profit+=max_price-nums[i]
    print(profit)
