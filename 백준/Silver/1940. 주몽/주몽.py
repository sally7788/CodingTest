n=int(input())
m=int(input())
nums=list(map(int,input().split()))
nums.sort()

left=0
right=n-1
cnt=0

while left < right:
    hap=nums[left]+nums[right]
    
    if hap==m:
        cnt+=1
        left+=1
        right-=1    
    
    elif hap < m:
        left+=1
    else:
        right-=1

print(cnt)