import sys
input=sys.stdin.readline

n,x=map(int,input().split())
days=list(map(int, input().split()))

current=sum(days[:x])
max_visitor=current
cnt=1

for i in range(x,n):
    current += days[i]
    current -= days[i-x]

    if current > max_visitor:
        max_visitor=current
        cnt=1
    elif current == max_visitor:
        cnt+=1

if max_visitor == 0:
    print("SAD")
else: 
    print(max_visitor)
    print(cnt)