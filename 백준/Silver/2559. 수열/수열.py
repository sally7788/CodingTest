import sys
input=sys.stdin.readline

n,k=map(int, input().split())
temp=list(map(int, input().split()))

curr=sum(temp[:k])
max_temp=curr

for i in range(k,n):
    curr += temp[i]
    curr -= temp[i-k]

    if curr > max_temp :
        max_temp=curr
print(max_temp)