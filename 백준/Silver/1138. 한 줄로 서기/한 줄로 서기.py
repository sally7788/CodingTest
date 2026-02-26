n=int(input())
height=list(map(int, input().split()))
ans=[]
for i in range(n-1,-1,-1):
    ans.insert(height[i],i+1) 
print(*ans)