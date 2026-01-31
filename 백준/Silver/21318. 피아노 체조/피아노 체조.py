import sys
input=sys.stdin.readline

n=int(input())
hard=list(map(int,input().split()))
q=int(input())

psum=[0]*(n+1)

for i in range(2, n+1):
    psum[i]=psum[i-1] + (1 if hard[i-2] > hard[i-1] else 0)

for _ in range(q):
    x,y=map(int, input().split())
    print(psum[y]-psum[x])