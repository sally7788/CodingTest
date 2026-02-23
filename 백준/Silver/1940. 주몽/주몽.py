n=int(input())
m=int(input())
nums=list(map(int,input().split()))
nums.sort()

left=0
right=n-1
cnt=0

while left < right:
    hap=nums[left]+nums[right]
    mid=(left+right) // 2
    if hap==m:
        cnt+=1    
    if hap < m:
        left+=1
    else:
        right-=1

print(cnt)
        

