import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
place=list(map(int,input().split()))

ans=max(place[0], n-place[-1])

for i in range(m-1):
    ans=max(ans, (place[i+1]-place[i]+1)//2)
print(ans)

