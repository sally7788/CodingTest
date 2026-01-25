n=int(input())
item=list(map(int,input().split()))
answer=[]
for height in range(n,0,-1):
    answer.insert(item[height-1],height)
print(*answer)